import os
import time
import io
import re
import pickle
import glob
import yaml
import argparse
import warnings

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Import from utils
from utils import (
    sanitize, pdf_to_notes, extract_lecture_metadata, 
    generate_lecture_filename, summarize_category, BLACKLIST,
    get_google_services
)

# --- CONFIGURATION ---
TARGET_IDS = ["MA103", "MA104", "DISCRETE"]

def is_likely_lecture(filename, title, topic):
    """Check if a file is likely to be a lecture based on keywords."""
    f = filename.lower()
    t = title.lower()
    top = topic.lower()
    
    # First, check the BLACKLIST
    if any(word in f or word in t or word in top for word in BLACKLIST):
        return False
    
    # For Discrete Mathematics and other large courses, we want to be selective
    # However, some files might just be named "historical_perspectives.pdf"
    # So we only reject if it looks like a problem set/assignment.
    return True

def main():
    parser = argparse.ArgumentParser(description='Sync Classroom PDFs to Docusaurus.')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files.')
    parser.add_argument('--filter', type=str, help='Only process files/categories matching this substring.')
    parser.add_argument('--course', type=str, help='Only process this specific course name/ID.')
    parser.add_argument('--summarize', action='store_true', help='Generate Master Summaries.')
    args = parser.parse_args()

    classroom, drive = get_google_services()
    courses = classroom.courses().list().execute().get('courses', [])
    all_summaries = {}

    for course in courses:
        raw_name = course.get('name', 'Unknown')
        clean_name = raw_name.replace("_", "").replace(" ", "").upper()
        
        if args.course:
            if args.course.upper() not in clean_name: continue
        elif not any(target in clean_name for target in TARGET_IDS): 
            continue

        course_name = sanitize(raw_name)
        course_clean = sanitize(course_name.replace("_", " "))
        print(f"\n>> Synchronizing: {course_clean}")
        
        try:
            topics_res = classroom.courses().topics().list(courseId=course['id']).execute()
            topic_map = {t['topicId']: t.get('name', 'Uncategorized') for t in topics_res.get('topic', [])}
            materials = classroom.courses().courseWorkMaterials().list(courseId=course['id']).execute().get('courseWorkMaterial', [])
            
            for m in materials:
                material_title = m.get('title', 'Untitled')
                topic_folder_raw = topic_map.get(m.get('topicId'), "Uncategorized")
                
                for attachment in m.get('materials', []):
                    if 'driveFile' in attachment:
                        f_data = attachment['driveFile'].get('driveFile', {})
                        original_filename = f_data.get('title') or f_data.get('name') or 'file.pdf'
                        
                        if not original_filename.lower().endswith(".pdf"): continue
                        if args.filter and args.filter.lower() not in original_filename.lower(): continue

                        # STRICTOR FILTERING
                        if not is_likely_lecture(original_filename, material_title, topic_folder_raw):
                            print(f"   [SKIP] Not a lecture: {original_filename}")
                            continue

                        print(f"   Downloading: {original_filename}")
                        download_success = False
                        for attempt in range(3):
                            try:
                                request = drive.files().get_media(fileId=f_data['id'])
                                with io.FileIO("temp.pdf", 'wb') as fh:
                                    downloader = MediaIoBaseDownload(fh, request, chunksize=1024*1024)
                                    done = False
                                    while not done: _, done = downloader.next_chunk()
                                download_success = True; break
                            except: time.sleep(3)
                        
                        if not download_success: continue

                        lec_hint = None
                        match = re.search(r'(?:SVC|Lec|Lecture)\D*(\d+)', original_filename, re.IGNORECASE)
                        if match: lec_hint = match.group(1)
                        
                        is_math_course = any(k in clean_name for k in ["MA", "ES", "DISCRETE"])
                        
                        md_text = pdf_to_notes("temp.pdf", original_filename, is_math=is_math_course, 
                                               course_name=course_name, category_hint=topic_folder_raw,
                                               lec_hint=lec_hint, is_extra_file=("extra" in original_filename.lower()),
                                               allow_large_split=True)
                        
                        if md_text:
                            for seg in md_text.split("<!-- LECTURE_SPLIT -->"):
                                seg = seg.strip()
                                if not seg: continue
                                lec_num, lec_name, category = extract_lecture_metadata(seg)
                                category = category or topic_folder_raw

                                if args.summarize:
                                    fm_match = re.search(r'---\s*(.*?)\s*---', seg, re.DOTALL)
                                    if fm_match:
                                        fm = yaml.safe_load(fm_match.group(1))
                                        if fm.get('summary'):
                                            key = (course_clean, category)
                                            if key not in all_summaries: all_summaries[key] = []
                                            all_summaries[key].append(fm.get('summary'))

                                out_dir = os.path.join("docs", course_clean, sanitize(category)) if category else os.path.join("docs", course_clean)
                                os.makedirs(out_dir, exist_ok=True)

                                filename = generate_lecture_filename(original_filename, lec_num, lec_name)
                                out_file = os.path.join(out_dir, f"{filename}.md")
                                if os.path.exists(out_file) and not args.force: continue
                                with open(out_file, "w", encoding="utf-8") as f: f.write(seg)
                                print(f"   [DONE] Saved: {filename}.md")
                        time.sleep(1)
        except Exception as e: print(f"   Error in {course_clean}: {e}")

    if args.summarize:
        for (course, category), summaries in all_summaries.items():
            master_md = summarize_category(course, category, summaries)
            if master_md:
                out_path = os.path.join("docs", sanitize(course), sanitize(category), "Summary.md") if category else os.path.join("docs", sanitize(course), "Summary.md")
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                final_text = f"---\ntitle: |\n  Summary: {category or course}\nsidebar_label: Summary\nsidebar_position: 0\n---\n\n{master_md}"
                with open(out_path, "w", encoding="utf-8") as f: f.write(final_text)

if __name__ == "__main__": main()
