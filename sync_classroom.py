import os
import time
import io
import re
import pickle
import warnings
import glob

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
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean.strip().replace(" ", "_").replace(".", "_")

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
    latex_instruction = "Format inline math as $...$ and display math as $$...$$."

    # Core structured prompt used for both math and non-math lectures
    prompt_base = (
        "You are an expert academic assistant producing high-quality lecture notes.\n"
        "Output a single Markdown document. Start with a YAML front-matter block with keys:\n"
        "title, course, topic, date (ISO), tags (list), summary (one-line), math: true/false, key_formulas (list of {name, formula, note}).\n"
        "After the front-matter, include these sections with H2 headings: Overview, Detailed Notes, Key Formulas, Examples (if any), Quick Summary.\n"
        "Format all math using LaTeX with the following instruction: " + latex_instruction + "\n"
        "In 'Key Formulas' include each formula in LaTeX and a short 1-line explanation.\n"
        "At the end include a Quick Summary (3-6 bullets).\n"
        "Also include a JSON blob inside an HTML comment labelled <!--KEY_FORMULAS_JSON--> containing the key_formulas array.\n"
        "Be concise, well-structured, and use clear headings."
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
        prompt = "Lecture Notes. Emphasize core ideas, examples, and intuition.\n" + prompt_base

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
                        try:
                            genai.delete_file(uploaded_file.name)
                        except:
                            pass
                        return response.text
                except Exception as e:
                    print(f"      [!] Model {model_id} error: {str(e)[:80]}")
                    continue
        except Exception as e:
            print(f"      [!] AI Attempt {attempt+1} failed: {e}")
            time.sleep(2)
    return None

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
                        original_filename = f_data.get('title', 'file.pdf')
                        
                        if original_filename.lower().endswith(".pdf"):
                            pdf_name_clean = sanitize(original_filename.replace(".pdf", "").replace(".PDF", ""))
                            out_dir = os.path.join("docs", course_name, sanitize(topic_folder_raw))
                            out_file = os.path.join(out_dir, f"{pdf_name_clean}.md")
                            
                            if os.path.exists(out_file): continue

                            print(f"   Downloading: {original_filename}")
                            request = drive.files().get_media(fileId=f_data['id'])
                            with io.FileIO("temp.pdf", 'wb') as fh:
                                MediaIoBaseDownload(fh, request).next_chunk()
                            
                            os.makedirs(out_dir, exist_ok=True)
                            md_text = pdf_to_notes("temp.pdf", original_filename, is_math=is_math)
                            
                            if md_text:
                                with open(out_file, "w", encoding="utf-8") as f:
                                    f.write(md_text)
                                print(f"   [DONE] Saved: {pdf_name_clean}.md")
                            time.sleep(1)

        except Exception as e:
            print(f"   Error in {course_name}: {e}")

    print("\n--- All Done! ---")

if __name__ == "__main__":
    main()