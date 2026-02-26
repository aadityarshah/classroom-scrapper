import os
import time
import io
import re
import pickle
import warnings
import glob
import yaml

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
TARGET_IDS = ["MA103", "MA104", "ES116"]

MODELS_TO_TRY = ["models/gemini-2.5-flash", "models/gemini-2.0-flash", "models/gemini-1.5-flash"]
BLACKLIST = ["tut", "solution", "assignment", "problem set", "quiz", "exam", "answer", "lab", "practice"]

genai.configure(api_key=GEMINI_API_KEY)

def sanitize(name):
    if not name: return "General"
    # Keep spaces, remove only truly illegal path chars
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean.strip()

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

def pdf_to_notes(pdf_path, filename, is_math=False, course_name=None, topic_folder=None):
    """Generate structured Markdown from a PDF using Gemini.

    Produces Markdown that begins with a YAML front-matter block containing:
    title, course, topic, date, tags, summary, math: true/false, key_formulas.
    Also includes a HTML comment block <!--KEY_FORMULAS_JSON--> containing
    the `key_formulas` array in JSON for programmatic parsing.
    """
    print(f"    --- AI processing: {filename} (Math: {is_math}) ...")

    # Prefer KaTeX-friendly delimiters; instruct both inline and block formats
    latex_instruction = (
        "Format ALL math using LaTeX. Use single dollar signs for inline math (e.g., $E=mc^2$) "
        "and double dollar signs for block math (e.g., $$a^2 + b^2 = c^2$$). "
        "Do NOT escape the dollar signs. Do NOT use code blocks for math."
    )

    # Core structured prompt used for both math and non-math lectures
    prompt_base = (
        "You are an expert academic assistant producing short, concise lecture notes.\n"
        "Output a single Markdown document. Start with a YAML front-matter block enclosed in '---'.\n"
        "CRITICAL: Use the YAML literal block scalar style (a pipe '|' followed by a NEWLINE and INDENTATION) "
        "for ALL string values. Example:\n"
        "---\n"
        "title: |\n"
        "  Lecture Title Here\n"
        "tags:\n"
        "  - |\n"
        "    Calculus\n"
        "---\n\n"
        "STRICT CONTENT RULES:\n"
        "1. Only include topics explicitly covered in the provided PDF.\n"
        "2. Do NOT add examples.\n"
        "3. Do NOT add outside information.\n"
        "4. Be extremely concise.\n\n"
        "STRUCTURE:\n"
        "- YAML Front-matter (keys: title, lecture_number, lecture_name, sidebar_label, course, topic, date, tags, summary, math: true, table_of_contents).\n"
        "  CRITICAL: sidebar_label must be exactly 'Lecture X' where X is the lecture number.\n"
        "- # Title (matching front-matter title)\n"
        "- ## Table of Contents\n"
        "- Sections (matching the TOC as H2 headings)\n"
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
                    response = model.generate_content([prompt, uploaded_file], request_options={"timeout": 160})
                    if response.text:
                        text = response.text
                        # Clean triple backticks if model wraps the whole response
                        if text.strip().startswith("```"):
                            # Remove the first line (e.g. ```markdown) and the last line (```)
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
            time.sleep(2)
    return None

def extract_lecture_metadata(markdown_content):
    """Parse YAML front-matter to extract lecture_number and lecture_name.
    
    Returns a tuple (lecture_number, lecture_name) or (None, None) if not found.
    """
    try:
        if markdown_content.startswith("---"):
            end_index = markdown_content.find("---", 3)
            if end_index != -1:
                yaml_block = markdown_content[3:end_index].strip()
                try:
                    front_matter = yaml.safe_load(yaml_block)
                    if front_matter:
                        return front_matter.get("lecture_number"), front_matter.get("lecture_name")
                except:
                    # Fallback regex if YAML parsing fails
                    num_match = re.search(r"lecture_number:\s*\|?\s*(\d+)", yaml_block)
                    name_match = re.search(r"lecture_name:\s*\|?\s*['\"]?(.*?)['\"]?\s*$", yaml_block, re.MULTILINE)
                    
                    lec_num = num_match.group(1) if num_match else None
                    lec_name = name_match.group(1).strip() if name_match else None
                    return lec_num, lec_name
    except Exception as e:
        print(f"      [!] Metadata extraction error: {e}")
    return None, None

def generate_lecture_filename(original_filename, lecture_number, lecture_name):
    """Generate a clean filename from lecture metadata.
    
    Examples:
    - (1, 'Series and Convergence') -> 'Lec_01_Series_and_Convergence'
    - ('2', 'Calculus Fundamentals') -> 'Lec_02_Calculus_Fundamentals'
    """
    if lecture_number is not None and lecture_name:
        # Format lecture_number as 2-digit zero-padded
        if isinstance(lecture_number, str):
            lec_num = lecture_number.strip()
            try:
                lec_num = str(int(float(lec_num))).zfill(2)
            except:
                pass
        else:
            lec_num = str(int(lecture_number)).zfill(2) if lecture_number else "00"
        
        # Sanitize lecture_name
        clean_name = sanitize(lecture_name)
        return f"Lec_{lec_num}_{clean_name}"
    
    # Fallback: sanitize original filename
    fname = original_filename.replace(".pdf", "").replace(".PDF", "")
    return sanitize(fname)

def main():
    classroom, drive = get_services()
    print("Fetching courses from Classroom...")
    courses = classroom.courses().list().execute().get('courses', [])

    for course in courses:
        raw_name = course.get('name', 'Unknown')
        
        # FUZZY FILTER: Remove spaces/underscores for comparison
        clean_name = raw_name.replace("_", "").replace(" ", "").upper()
        
        match = False
        for target in TARGET_IDS:
            if target in clean_name:
                match = True
                break
        
        if not match:
            continue

        is_math = "MA" in clean_name
        course_name = sanitize(raw_name)
        print(f"\n>> Synchronizing: {course_name} (Math: {is_math})")
        
        try:
            topics_res = classroom.courses().topics().list(courseId=course['id']).execute()
            topic_map = {t['topicId']: t.get('name', 'Uncategorized') for t in topics_res.get('topic', [])}

            materials_res = classroom.courses().courseWorkMaterials().list(courseId=course['id']).execute()
            materials = materials_res.get('courseWorkMaterial', [])
            
            for m in materials:
                material_title = m.get('title', 'Untitled')
                topic_id = m.get('topicId')
                topic_folder_raw = topic_map.get(topic_id, "Uncategorized")

                if any(word in material_title.lower() or word in topic_folder_raw.lower() for word in BLACKLIST):
                    continue

                for attachment in m.get('materials', []):
                    if 'driveFile' in attachment:
                        f_data = attachment['driveFile']['driveFile']
                        original_filename = f_data.get('name', f_data.get('title', 'file.pdf'))
                        
                        if original_filename.lower().endswith(".pdf"):
                            course_dir = sanitize(course_name.replace("_", " "))
                            topic_dir = sanitize(topic_folder_raw)
                            
                            if topic_dir.lower() == "uncategorized":
                                out_dir = os.path.join("docs", course_dir)
                            else:
                                out_dir = os.path.join("docs", course_dir, topic_dir)
                            
                            if not os.path.exists(out_dir):
                                os.makedirs(out_dir, exist_ok=True)

                            print(f"   Downloading: {original_filename}")
                            request = drive.files().get_media(fileId=f_data['id'])
                            with io.FileIO("temp.pdf", 'wb') as fh:
                                MediaIoBaseDownload(fh, request).next_chunk()
                            
                            # Pass course and topic context to pdf_to_notes for AI smart naming
                            md_text = pdf_to_notes("temp.pdf", original_filename, is_math=is_math, 
                                                   course_name=course_name, topic_folder=topic_folder_raw)
                            
                            if md_text:
                                # Extract lecture metadata for smart naming
                                lecture_number, lecture_name = extract_lecture_metadata(md_text)
                                filename = generate_lecture_filename(original_filename, lecture_number, lecture_name)
                                out_file = os.path.join(out_dir, f"{filename}.md")
                                
                                # Check if this smart-named file already exists
                                if os.path.exists(out_file):
                                    print(f"   [SKIP] Already exists: {filename}.md")
                                    continue
                                
                                with open(out_file, "w", encoding="utf-8") as f:
                                    f.write(md_text)
                                
                                # Display both original and smart-named versions
                                display_name = lecture_name if lecture_name else filename
                                print(f"   [DONE] Saved: {filename}.md ({display_name})")
                            time.sleep(1)

        except Exception as e:
            print(f"   Error in {course_name}: {e}")

    print("\n--- All Done! ---")

if __name__ == "__main__":
    main()