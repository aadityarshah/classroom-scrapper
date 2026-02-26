import os
import time
import io
import re
import pickle
import warnings
import glob

# Mute the deprecation warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# --- CONFIGURATION ---
# IMPORTANT: the Gemini API key is stored in a separate module `api_key.py`
# that is ignored by version control.  Edit that file with your actual key.
from api_key import GEMINI_API_KEY

# Using the EXACT strings from your model list
# Primary: 2.5 Flash (Fast), Secondary: 3.1 Pro (Reasoning/Summary)
MODELS_TO_TRY = [
    "models/gemini-2.5-flash",
    "models/gemini-2.0-flash",
    "models/gemini-1.5-flash"
]
SUMMARY_MODEL = "models/gemini-3.1-pro-preview"

SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly',
    'https://www.googleapis.com/auth/classroom.topics.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

genai.configure(api_key=GEMINI_API_KEY)

def sanitize(name):
    """Deep clean for Windows folder/file names."""
    if not name: return "General"
    # Remove characters Windows/MkDocs dislike: \ / : * ? " < > |
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean.strip().replace(" ", "_").replace(".", "_")

def get_services():
    """Handles OAuth login and token storage."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('classroom', 'v1', credentials=creds), build('drive', 'v3', credentials=creds)

def pdf_to_notes(pdf_path, title):
    """Uploads PDF to Gemini and generates high-quality Markdown."""
    print(f"    --- AI processing PDF: {title} ...")
    try:
        # 1. Upload to Gemini
        uploaded_file = genai.upload_file(path=pdf_path)
        
        # 2. WAIT for parsing (Max 30 seconds)
        retries = 0
        while uploaded_file.state.name == "PROCESSING" and retries < 10:
            time.sleep(3)
            uploaded_file = genai.get_file(uploaded_file.name)
            retries += 1
            
        if uploaded_file.state.name == "FAILED":
            return None

        # 3. Try models in order (using Flash for speed)
        for model_id in MODELS_TO_TRY:
            try:
                print(f"    --- Using model: {model_id}")
                model = genai.GenerativeModel(model_name=model_id)
                
                prompt = (
                    "You are an expert academic assistant at IITGN. Study this PDF and: \n"
                    "1. Create structured Markdown notes with clear headings.\n"
                    "2. Format all mathematical equations in perfect LaTeX using $...$.\n"
                    "3. Highlight key formulas and recurring themes.\n"
                    "4. Include a 'Quick Summary' table at the end."
                )
                
                # Timeout added to prevent hangs
                response = model.generate_content([prompt, uploaded_file], 
                                                  request_options={"timeout": 120})
                
                if response.text:
                    try: genai.delete_file(uploaded_file.name)
                    except: pass
                    return response.text
            except Exception as e:
                print(f"      [!] Model error: {str(e)[:50]}")
                continue
        
        return None
    except Exception as e:
        print(f"      [!!!] AI Upload System Error: {e}")
        return None

def generate_master_summary(course_dir, course_name):
    """Uses the smartest model (3.1 Pro) to summarize the whole course folder."""
    md_files = glob.glob(f"{course_dir}/**/*.md", recursive=True)
    md_files = [f for f in md_files if "Summary.md" not in f]
    
    if len(md_files) < 2: return

    print(f"    --- Creating Master Summary for {course_name} using 3.1 Pro...")
    combined_context = ""
    for f_path in md_files[:6]: # Use snippets from 6 lectures
        try:
            with open(f_path, 'r', encoding='utf-8') as f:
                combined_context += f"\nLecture {os.path.basename(f_path)}:\n" + f.read()[:1000]
        except: continue

    prompt = (
        f"Based on these lecture snippets for {course_name}, write a 1-page Master Course Summary. "
        "Summarize the learning journey so far and list the 5 most important formulas or concepts."
    )
    
    try:
        model = genai.GenerativeModel(model_name=SUMMARY_MODEL)
        response = model.generate_content(prompt + combined_context)
        with open(os.path.join(course_dir, "Summary.md"), "w", encoding='utf-8') as f:
            f.write(f"# 🎓 Master Summary: {course_name.replace('_', ' ')}\n\n")
            f.write(response.text)
        print("    [DONE] Summary generated.")
    except: pass

def main():
    classroom, drive = get_services()
    print("Starting Sync...")
    
    courses = classroom.courses().list().execute().get('courses', [])

    for course in courses:
        course_name = sanitize(course['name'])
        print(f"\n>> Synchronizing: {course_name}")
        
        try:
            # Get Topics (Lecture grouping)
            topics_res = classroom.courses().topics().list(courseId=course['id']).execute()
            topic_map = {t['topicId']: sanitize(t['name']) for t in topics_res.get('topic', [])}

            materials_res = classroom.courses().courseWorkMaterials().list(courseId=course['id']).execute()
            materials = materials_res.get('courseWorkMaterial', [])
            
            for m in materials:
                topic_folder = topic_map.get(m.get('topicId'), "General_Lectures")
                title = sanitize(m.get('title', 'Untitled'))
                
                for attachment in m.get('materials', []):
                    if 'driveFile' in attachment:
                        f_data = attachment['driveFile']['driveFile']
                        if f_data['title'].lower().endswith(".pdf"):
                            
                            # Standardize directory paths
                            out_dir = os.path.join("docs", course_name, topic_folder)
                            out_file = os.path.join(out_dir, f"{title}.md")
                            
                            if os.path.exists(out_file):
                                continue

                            print(f"   Downloading: {f_data['title']}")
                            request = drive.files().get_media(fileId=f_data['id'])
                            
                            # Using temp.pdf locally
                            with io.FileIO("temp.pdf", 'wb') as fh:
                                MediaIoBaseDownload(fh, request).next_chunk()

                            os.makedirs(out_dir, exist_ok=True)
                            md_text = pdf_to_notes("temp.pdf", title)
                            
                            if md_text:
                                with open(out_file, "w", encoding="utf-8") as f:
                                    f.write(md_text)
                                print(f"   [DONE] Saved: {title}.md")
                            
                            time.sleep(2)

            # Generate Summary once course materials are processed
            generate_master_summary(os.path.join("docs", course_name), course_name)

        except Exception as e:
            print(f"   Skipping {course_name}: {e}")

    print("\n--- All Done! ---")

if __name__ == "__main__":
    main()