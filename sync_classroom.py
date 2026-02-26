import os
import time
import io
import re
import pickle
import warnings
import glob
import yaml
import argparse

# Mute warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# --- CONFIGURATION ---
from api_key import GEMINI_API_KEY

# We will look for these IDs regardless of spaces or underscores
TARGET_IDS = ["MA103", "MA104"]

MODELS_TO_TRY = ["models/gemini-2.5-flash", "models/gemini-1.5-flash"]
BLACKLIST = ["tut", "solution", "assignment", "problem set", "quiz", "exam", "answer", "lab", "practice"]

genai.configure(api_key=GEMINI_API_KEY)

def sanitize(name):
    if not name: return "General"
    # Keep spaces, remove only truly illegal path chars, and strip ALL types of newlines
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean.replace("\n", " ").replace("\r", "").strip()

def get_services():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', [
                'https://www.googleapis.com/auth/classroom.courses.readonly',
                'https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly',
                'https://www.googleapis.com/auth/classroom.topics.readonly',
                'https://www.googleapis.com/auth/drive.readonly'
            ])
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('classroom', 'v1', credentials=creds), build('drive', 'v3', credentials=creds)

def pdf_to_notes(pdf_path, filename, is_math=False, course_name=None, topic_folder=None, lec_hint=None, is_extra_file=False):
    """Generate structured Markdown from a PDF using Gemini."""
    print(f"    --- AI processing: {filename} (Math: {is_math}) ...")

    # Prefer KaTeX-friendly delimiters; instruct both inline and block formats
    latex_instruction = (
        "Format ALL math using LaTeX. Use single dollar signs for inline math (e.g., $E=mc^2$) "
        "and double dollar signs for block math (e.g., $$a^2 + b^2 = c^2$$). "
        "Do NOT escape the dollar signs. Do NOT use code blocks for math."
    )

    # Build specialized instructions based on filename analysis
    hint_instruction = ""
    if is_extra_file:
        hint_instruction = "CRITICAL: This is an EXTRA material file. Set lecture_number to 999.\n"
    elif lec_hint:
        hint_instruction = f"CRITICAL: The filename suggests this is Lecture {lec_hint}. Prioritize this number for the lecture_number field.\n"

    # Core structured prompt used for both math and non-math lectures
    prompt_base = (
        "You are an expert academic revision assistant producing punchy, highly concise lecture notes.\n"
        "Output a single Markdown document (or multiple if split).\n"
        "Start with a YAML front-matter block enclosed in '---'.\n"
        "CRITICAL YAML RULE: Use the pipe '|' for EVERY string value. THE PIPE MUST BE FOLLOWED IMMEDIATELY BY A NEWLINE. "
        "The string content must start on the NEXT line, indented by two spaces.\n"
        "Example:\n"
        "title: |\n"
        "  My Correct Title\n\n"
        "STRICT CONTENT RULES:\n"
        "1. ONLY include topics explicitly covered in the PDF.\n"
        "2. Do NOT add examples.\n"
        "3. Do NOT add outside information or long derivations.\n"
        "4. STRICT LENGTH: Summarize each section into a single concise paragraph or high-value bullet points.\n"
        "5. Be direct and minimalist.\n"
        "6. CRITICAL: Never use raw '<' or '>' signs. Always use LaTeX versions '$<$' and '$>$' even in headings.\n\n"
        "CATEGORIZATION:\n"
        + hint_instruction +
        "- Identify if the course has distinct major sub-sections (e.g., MA103 is split into 'Single Variable Calculus' and 'Linear Algebra').\n"
        "- If it's a distinct sub-section, put it in 'category'. Otherwise, leave 'category' empty (CRITICAL: Do not just repeat the course name).\n"
        "- If it is a standard lecture, assign its lecture_number (1, 2, 3...).\n"
        "- If it is extra material (contains 'extra' in filename), set lecture_number to 999 and sidebar_label to its descriptive name (e.g., 'Syllabus').\n"
        "- If the PDF covers multiple distinct lectures (e.g., Lec 9 AND 10), provide TWO full Markdown documents, separated by: <!-- LECTURE_SPLIT -->\n\n"
        "STRUCTURE PER DOCUMENT:\n"
        "- YAML Front-matter (keys: title, lecture_number, lecture_name, category, sidebar_label, sidebar_position, course, topic, tags, summary, math: true).\n"
        "  CRITICAL: Do NOT include a 'date' field.\n"
        "  CRITICAL: 'tags' must be a YAML block sequence (one per line with a dash). Example:\n"
        "  tags:\n"
        "    - Math\n"
        "    - Calculus\n"
        "  CRITICAL: sidebar_label must be 'Lecture X'. sidebar_position must be the integer lecture_number.\n"
        "  CRITICAL: lecture_name must be the TOPIC only, NOT the word 'Lecture X'.\n"
        "- # Title (matching front-matter title)\n"
        "- ## Table of Contents (followed by a simple bulleted list of the sections below)\n"
        "- Lecture Content (create an H2 heading for each item in the Table of Contents, then provide the content for that section. Keep content extremely short and dense.)\n"
        "- ## Key Formulas\n"
        "- ## Quick Summary\n\n"
        "Format ALL math using LaTeX ($...$ or $$...$$). Do NOT use code blocks for math. Use clear, hierarchical headings."
    )

    # Add contextual metadata so the model can fill front-matter
    if course_name:
        prompt_base += f"\nCourse: {course_name.replace('_', ' ')}"
    if topic_folder:
        prompt_base += f"\nTopic: {topic_folder.replace('_', ' ')}"

    # Slightly different emphasis for math courses
    if is_math:
        prompt = "Mathematics Lecture Notes. Emphasize definitions, theorems, and central formulas.\n" + prompt_base
    else:
        prompt = "Lecture Notes. Emphasize core ideas and intuition.\n" + prompt_base

    for attempt in range(2):
        try:
            uploaded_file = genai.upload_file(path=pdf_path)
            retries = 0
            while uploaded_file.state.name == "PROCESSING" and retries < 10:
                time.sleep(2)
                uploaded_file = genai.get_file(uploaded_file.name)
                retries += 1

            if uploaded_file.state.name == "FAILED":
                print("      [!] Upload failed or parsing error.")
                return None

            for model_id in MODELS_TO_TRY:
                try:
                    model = genai.GenerativeModel(model_name=model_id)
                    response = model.generate_content([prompt, uploaded_file], request_options={"timeout": 300})
                    if response.text:
                        text = response.text
                        # Clean triple backticks if model wraps the whole response
                        if text.strip().startswith("```"):
                            lines = text.strip().split("\n")
                            if lines[0].startswith("```"):
                                lines = lines[1:]
                            if lines[-1].strip() == "```":
                                lines = lines[:-1]
                            text = "\n".join(lines).strip()
                        
                        try:
                            genai.delete_file(uploaded_file.name)
                        except:
                            pass
                        return text
                except Exception as e:
                    print(f"      [!] Model {model_id} error: {str(e)[:80]}")
                    continue
        except Exception as e:
            print(f"      [!] AI Attempt {attempt+1} failed: {e}")
            time.sleep(5)
    return None

def extract_lecture_metadata(markdown_content):
    """Parse YAML front-matter to extract metadata."""
    try:
        if markdown_content.startswith("---"):
            end_index = markdown_content.find("---", 3)
            if end_index != -1:
                yaml_block = markdown_content[3:end_index].strip()
                try:
                    front_matter = yaml.safe_load(yaml_block)
                    if front_matter:
                        return (front_matter.get("lecture_number"), 
                                front_matter.get("lecture_name"),
                                front_matter.get("category"))
                except:
                    # Fallback regex
                    num_match = re.search(r"lecture_number:\s*\|?\s*(\d+)", yaml_block)
                    name_match = re.search(r"lecture_name:\s*\|?\s*['\"]?(.*?)['\"]?\s*$", yaml_block, re.MULTILINE)
                    cat_match = re.search(r"category:\s*\|?\s*['\"]?(.*?)['\"]?\s*$", yaml_block, re.MULTILINE)
                    
                    lec_num = num_match.group(1).strip() if num_match else None
                    lec_name = name_match.group(1).strip() if name_match else None
                    category = cat_match.group(1).strip() if cat_match else None
                    return lec_num, lec_name, category
    except Exception as e:
        print(f"      [!] Metadata extraction error: {e}")
    return None, None, None

def generate_lecture_filename(original_filename, lecture_number, lecture_name):
    """Generate a clean filename."""
    if lecture_number is not None and lecture_name:
        if str(lecture_number) == "999":
            return f"Extra_{sanitize(lecture_name)}"
        # Ensure lecture_number is just digits before padding
        clean_num = re.sub(r'\D', '', str(lecture_number))
        lec_num = clean_num.zfill(2) if clean_num else "00"
        return f"Lec_{lec_num}_{sanitize(lecture_name)}"
    return sanitize(original_filename.replace(".pdf", "").replace(".PDF", ""))

def summarize_category(course_name, category_name, summaries):
    """Generate a Master Summary for a course category."""
    print(f"\n   >>> Generating Master Summary for: {course_name} - {category_name or 'Main'}")
    combined_summaries = "\n".join([f"- {s}" for s in summaries])
    prompt = (
        f"You are an academic lead summarizing: '{category_name or course_name}'.\n"
        f"Individual summaries:\n{combined_summaries}\n\n"
        "Produce a cohesive, high-level Master Summary (3-5 paragraphs) connecting these topics. "
        "Format as Markdown with a H1 title and NO front-matter."
    )
    for model_id in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_id)
            response = model.generate_content(prompt)
            if response.text: return response.text
        except: continue
    return None

def main():
    parser = argparse.ArgumentParser(description='Sync Classroom PDFs to Docusaurus.')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files.')
    parser.add_argument('--filter', type=str, help='Only process files/categories matching this substring.')
    parser.add_argument('--course', type=str, help='Only process this specific course ID (e.g., MA104).')
    parser.add_argument('--summarize', action='store_true', help='Generate Master Summaries.')
    args = parser.parse_args()

    classroom, drive = get_services()
    courses = classroom.courses().list().execute().get('courses', [])
    all_summaries = {}

    for course in courses:
        raw_name = course.get('name', 'Unknown')
        clean_name = raw_name.replace("_", "").replace(" ", "").upper()
        
        # Priority Filter: Specific Course ID
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
                if any(word in material_title.lower() or word in topic_folder_raw.lower() for word in BLACKLIST): continue

                for attachment in m.get('materials', []):
                    if 'driveFile' in attachment:
                        f_data = attachment['driveFile'].get('driveFile', {})
                        original_filename = f_data.get('title') or f_data.get('name') or 'file.pdf'
                        if args.filter and args.filter.lower() not in original_filename.lower(): continue
                        if not original_filename.lower().endswith(".pdf"): continue

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
                        is_extra_file = "extra" in original_filename.lower()

                        md_text = pdf_to_notes("temp.pdf", original_filename, is_math=("MA" in clean_name), 
                                               course_name=course_name, topic_folder=topic_folder_raw,
                                               lec_hint=lec_hint, is_extra_file=is_extra_file)
                        
                        if md_text:
                            # Post-process to fix Docusaurus build crashes caused by raw < and >
                            # We replace them globally with LaTeX versions unless they are likely HTML tags
                            processed_segments = []
                            segments = md_text.split("<!-- LECTURE_SPLIT -->")
                            for seg in segments:
                                seg = seg.strip()
                                if not seg: continue
                                
                                # Replace < and > with LaTeX versions
                                # We skip common HTML tags if the AI accidentally generates them
                                seg = seg.replace("< ", " $<$ ").replace(" >", " $>$ ")
                                # Handle cases like (n<0)
                                seg = re.sub(r'([a-zA-Z0-9])<([a-zA-Z0-9])', r'\1 $<$ \2', seg)
                                seg = re.sub(r'([a-zA-Z0-9])>([a-zA-Z0-9])', r'\1 $>$ \2', seg)
                                
                                processed_segments.append(seg)
                            
                            for seg in processed_segments:
                                lec_num, lec_name, category = extract_lecture_metadata(seg)
                                
                                if args.summarize:
                                    try:
                                        fm = yaml.safe_load(seg[3:seg.find("---", 3)])
                                        s_val = fm.get('summary', '')
                                        if s_val:
                                            key = (course_clean, category)
                                            if key not in all_summaries: all_summaries[key] = []
                                            all_summaries[key].append(s_val)
                                    except: pass

                                simple_course = re.sub(r'^[A-Z0-9]+\s*', '', course_clean).lower()
                                use_subfolder = False
                                if category:
                                    cat_clean = sanitize(category).lower()
                                    if cat_clean not in ["uncategorized", course_clean.lower(), simple_course, "ordinary differential equations", "calculus"]:
                                        if cat_clean not in simple_course and simple_course not in cat_clean:
                                            use_subfolder = True

                                out_dir = os.path.join("docs", course_clean, sanitize(category)) if use_subfolder else os.path.join("docs", course_clean)
                                if not os.path.exists(out_dir): os.makedirs(out_dir, exist_ok=True)

                                filename = generate_lecture_filename(original_filename, lec_num, lec_name)
                                seg = re.sub(r' < ', ' &lt; ', seg)
                                seg = re.sub(r' > ', ' &gt; ', seg)
                                out_file = os.path.join(out_dir, f"{filename}.md")
                                if os.path.exists(out_file) and not args.force: continue
                                with open(out_file, "w", encoding="utf-8") as f: f.write(seg)
                                print(f"   [DONE] Saved: {filename}.md in {category or 'root'}")
                        time.sleep(1)
        except Exception as e: print(f"   Error in {course_clean}: {e}")

    if args.summarize:
        print("\n   >>> Scanning existing docs for summaries...")
        for root, dirs, files in os.walk("docs"):
            for file in files:
                if file.endswith(".md") and file != "Summary.md":
                    # Check filters if provided
                    if args.course and args.course.lower() not in root.lower():
                        continue
                    if args.filter and args.filter.lower() not in root.lower() and args.filter.lower() not in file.lower():
                        continue
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            content = f.read()
                            if content.startswith("---"):
                                end_fm = content.find("---", 3)
                                fm = yaml.safe_load(content[3:end_fm])
                                s_val = fm.get('summary', '').replace("|", "").strip()
                                course = fm.get('course', 'Unknown').replace("|", "").strip()
                                category = fm.get('category', '').replace("|", "").strip()
                                if not category or category.lower() in ["none", ""]: category = None
                                if s_val:
                                    key = (course, category)
                                    if key not in all_summaries: all_summaries[key] = []
                                    if s_val not in all_summaries[key]: all_summaries[key].append(s_val)
                    except: continue

        for (course, category), summaries in all_summaries.items():
            if not summaries: continue
            if args.filter and args.filter.lower() not in (category or "").lower() and args.filter.lower() not in course.lower():
                continue
            master_md = summarize_category(course, category, summaries)
            if master_md:
                course_folder = sanitize(course)
                out_path = os.path.join("docs", course_folder, sanitize(category), "Summary.md") if category else os.path.join("docs", course_folder, "Summary.md")
                final_text = f"---\ntitle: |\n  Summary: {category or course}\nsidebar_label: Summary\nsidebar_position: 0\n---\n\n{master_md}"
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "w", encoding="utf-8") as f: f.write(final_text)
                print(f"   [CREATED] Master Summary for {course}/{category or 'root'}")

if __name__ == "__main__": main()
