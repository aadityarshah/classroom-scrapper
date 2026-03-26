import os
import sys
import time
import io
import re
import yaml
import pickle
import requests
import warnings
from datetime import date
import google.generativeai as genai
from bs4 import BeautifulSoup

# Add root to path for api_key
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from api_key import GEMINI_API_KEY
from pypdf import PdfReader
from urllib.parse import urljoin

# Mute warnings
warnings.filterwarnings("ignore")

# Use stable model IDs
MODELS_TO_TRY = ["gemini-2.5-flash", "gemini-flash-latest"]
BLACKLIST = ["tut", "solution", "assignment", "problem set", "quiz", "exam", "answer", "lab", "practice", "homework", "ps", "pset"]

genai.configure(api_key=GEMINI_API_KEY)

def get_google_services():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try: creds.refresh(Request())
            except: creds = None
        if not creds:
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

def sanitize(name):
    if not name: return ""
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean.replace("\n", " ").replace("\r", "").strip()

def get_pdf_page_count(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        return len(reader.pages)
    except: return 0

def analyze_page_structure(soup, base_url, course_name):
    print(f"    --- AI analyzing structural hierarchy for {course_name} ...", flush=True)
    structure_summary = []
    current_heading = "General"
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'a']):
        if element.name in ['h1', 'h2', 'h3', 'h4']:
            current_heading = element.get_text(strip=True)
        elif element.name == 'a' and element.get('href'):
            href = element.get('href')
            link_text = element.get_text(strip=True)
            if any(k in href.lower() for k in [".pdf", "drive.google", "sharepoint", "onedrive", ".html", ".htm"]):
                abs_url = urljoin(base_url, href)
                structure_summary.append(f"Heading: '{current_heading}' -> Link: '{link_text}' (URL: {abs_url})")

    print(f"    --- Found {len(structure_summary)} potential structured links. Sending to AI...", flush=True)
    prompt = (
        f"You are an expert academic organizer for '{course_name}'.\n"
        "Group links into Categories based strictly on page headings.\n"
        "Output ONLY valid YAML. Keys: URLs, Values: Category names.\n"
        "Category names should be clean and descriptive (e.g., 'Fundamentals', 'Circuit Analysis').\n"
        f"STRUCTURE:\n" + "\n".join(structure_summary[:200])
    )
    for model_id in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_id)
            print(f"    --- Attempting model {model_id} ...", flush=True)
            response = model.generate_content(prompt)
            if response.text:
                clean_text = response.text.replace("```yaml", "").replace("```", "").strip()
                if "---" in clean_text: clean_text = clean_text.split("---")[-1].strip()
                result = yaml.safe_load(clean_text) or {}
                print(f"    --- AI structure analysis complete. Found {len(result)} mappings.", flush=True)
                return result
        except Exception as e:
            print(f"    --- AI structure analysis error with {model_id}: {e}", flush=True)
            continue
    return {}

def fix_markdown_formatting(text):
    """Deeply clean and validate Markdown front-matter and content."""
    generated_date = date.today().strftime("%d %B %Y")
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r'^```[a-zA-Z]*\n', '', text)
        text = re.sub(r'\n```$', '', text)

    if not text.startswith("---"):
        lines = text.splitlines()
        first_header_idx = next((i for i, line in enumerate(lines) if line.lstrip().startswith("#")), None)
        if first_header_idx is not None:
            fm_candidate = "\n".join(line for line in lines[:first_header_idx] if line.strip() and line.strip() != "```").strip()
            content_candidate = "\n".join(lines[first_header_idx:]).strip()
            if "title:" in fm_candidate and "lecture_number:" in fm_candidate:
                text = f"---\n{fm_candidate}\n---\n\n{content_candidate}"

    if not text.startswith("---"): return text
    parts = text.split("---", 2)
    if len(parts) < 3: return text
    
    fm_raw = parts[1]
    content = parts[2]

    try:
        # Parse the AI's messy YAML
        data = yaml.safe_load(fm_raw)
        if not isinstance(data, dict): raise ValueError("Not a dict")
        
        # 1. CLEAN TITLE (No pipe, clean quotes)
        title = str(data.get('title', 'Lecture Notes')).strip()
        title = title.strip("'").strip('"').replace("|", "").strip()
        data['title'] = title

        # 2. STANDARDIZE SIDEBAR (Strictly 'Lecture X')
        lec_num = data.get('lecture_number', '0')
        data['sidebar_label'] = f"Lecture {lec_num}"
        data['sidebar_position'] = float(lec_num) if "." in str(lec_num) else int(lec_num)

        # 2.5. KEEP LAST UPDATED CONSISTENT FOR GENERATED NOTES
        data['last_updated'] = generated_date

        # 3. ENSURE ARRAYS
        for key in ['tags', 'topic']:
            val = data.get(key, [])
            if isinstance(val, str):
                data[key] = [item.strip() for item in val.split(",") if item.strip()]
            elif val is None:
                data[key] = []

        # 4. RE-GENERATE CLEAN YAML
        # Force quotes on specific string fields for Docusaurus/YAML safety
        class QuotedDumper(yaml.SafeDumper):
            def represent_data(self, data):
                if isinstance(data, str) and any(c in data for c in ":#{}[]|&*>!?'\""):
                    return self.represent_scalar('tag:yaml.org,2002:str', data, style='"')
                return super().represent_data(data)

        # We'll just use a simpler way: wrap the specific fields in quotes if they aren't already
        # Actually, yaml.dump with default_flow_style=False is usually fine, 
        # but let's ensure 'course' and 'title' are treated as strings and handled carefully.
        
        new_fm = yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)
        fm_final = f"---\n{new_fm}---\n"
    except Exception as e:
        print(f"      [!] Manual YAML repair triggered: {e}")
        # Fallback to regex if yaml.load fails
        fm_final = f"---{fm_raw}---"

    # 5. Fix < and > outside of LaTeX blocks in the content
    content_parts = re.split(r'(\$\$.*?\$\$|\$.*?\$)', content, flags=re.DOTALL)
    for i in range(len(content_parts)):
        if not content_parts[i].startswith('$'):
            content_parts[i] = content_parts[i].replace("<", "$<$").replace(">", "$>$")
    
    return fm_final + "".join(content_parts)

def pdf_to_notes(pdf_path, filename, is_math=False, course_name=None, category_hint=None, lec_hint=None, is_extra_file=False, allow_large_split=False, is_concise=False):
    page_count = get_pdf_page_count(pdf_path)
    if page_count > 200 and not (allow_large_split and "lecture" in filename.lower()): return None

    print(f"    --- AI processing: {filename} ({page_count} pages) ...")

    split_instruction = "### SPECIAL RULE: Large file. Split into docs with '<!-- LECTURE_SPLIT -->'.\n" if page_count > 200 else ""
    cat_instruction = f"### CATEGORY: '{category_hint}'.\n" if category_hint else ""
    lec_instruction = f"### LECTURE NUMBER: This is Lecture {lec_hint}.\n" if lec_hint else ""
    concise_instruction = (
        "### CONCISE MODE ACTIVE:\n"
        "- Generate compact study notes that preserve all core concepts and definitions.\n"
        "- DO NOT include worked examples, repeated intuition, long derivations, or implementation detail unless essential.\n"
        "- Compress each major topic into the minimum text needed for revision.\n"
        "- Prefer formulas, assumptions, conditions, and takeaways over narrative explanation.\n"
        "- The notes should feel like high-quality revision notes, not a transcript.\n"
    ) if is_concise else ""

    prompt_base = (
        "You are a world-class professor creating ELITE Docusaurus notes.\n\n"
        + split_instruction + cat_instruction + lec_instruction + concise_instruction +
        "## 1. YAML FRONT-MATTER RULES (STRICT):\n"
        "- EVERYTHING must be valid YAML.\n"
        "- ALL string values (especially 'course', 'title', 'lecture_name', 'category', 'summary') MUST be wrapped in double quotes (\").\n"
        "- Example: course: \"ES119 Principles of AI\"\n"
        "- 'title': NO pipe characters. Simple string in quotes.\n"
        "- 'tags' and 'topic': MUST be bulleted arrays.\n"
        "- 'sidebar_label': MUST be 'Lecture X'.\n"
        "- 'lecture_name': Descriptive human title (NO LaTeX or math symbols here).\n\n"
        "## 2. CONTENT RULES:\n"
        "- MANDATORY: End with '## Quick Summary' section.\n"
        "- Focus 85% on theory. High density, concise.\n"
        "- Cover all major concepts from the source, but compress aggressively.\n"
        "- Prefer short, information-dense sections over long explanations.\n"
        "- Include only essential examples. Omit routine or repetitive examples.\n"
        "- Do not restate the same idea in multiple ways.\n"
        "- Keep derivations brief unless a derivation is itself the key concept.\n"
        "- LaTeX: Use $...$ for inline and $$...$$ for blocks.\n"
        "- TOC COMPATIBILITY: Do NOT use LaTeX or backslashes in main section headers (#, ##, ###). Headers must be plain text only (use basic bold **text** if needed) to ensure they render correctly in the Table of Contents.\n"
        "KEYS: title, lecture_number, lecture_name, category, sidebar_label, sidebar_position, course, topic, tags, summary, math: true.\n"
    )

    prompt = ("### Mathematics Professor.\n" if is_math else "### Academic Professor.\n") + prompt_base + f"\nFILENAME: {filename}"

    for attempt in range(2):
        try:
            uploaded_file = genai.upload_file(path=pdf_path)
            retries = 0
            while uploaded_file.state.name == "PROCESSING" and retries < 15:
                time.sleep(2); uploaded_file = genai.get_file(uploaded_file.name); retries += 1

            for model_id in MODELS_TO_TRY:
                try:
                    model = genai.GenerativeModel(model_name=model_id)
                    print(f"      --- Calling {model_id} ...")
                    response = model.generate_content([prompt, uploaded_file], request_options={"timeout": 600})
                    print(f"      --- AI response received from {model_id}.")
                    try:
                        text = response.text
                        if text.strip().startswith("```"):
                            text = re.sub(r'^```[a-zA-Z]*\n', '', text.strip())
                            text = re.sub(r'\n```$', '', text)
                        try: genai.delete_file(uploaded_file.name)
                        except: pass
                        return fix_markdown_formatting(text)
                    except: continue
                except: continue
        except: time.sleep(5)
    return None

def extract_lecture_metadata(markdown_content):
    try:
        if markdown_content.startswith("---"):
            end_index = markdown_content.find("---", 3)
            if end_index != -1:
                yaml_block = markdown_content[3:end_index].strip()
                fm = yaml.safe_load(yaml_block)
                if fm: return fm.get("lecture_number"), fm.get("lecture_name"), fm.get("category")
    except: pass
    return None, None, None

def generate_lecture_filename(original_filename, lecture_number, lecture_name):
    if lecture_number is not None and lecture_name:
        clean_name = sanitize(lecture_name)
        if ": " in clean_name: clean_name = clean_name.split(": ", 1)[1]
        if str(lecture_number) == "999": return f"Extra_{clean_name}"
        lec_str = str(lecture_number).replace(".", "-")
        return f"Lec_{lec_str.zfill(2) if '-' not in lec_str else lec_str}_{clean_name}"
    return sanitize(original_filename.replace(".pdf", ""))

def generate_custom_summary(notes_content, user_prompt):
    full_context = "\n\n--- NEXT FILE ---\n\n".join(notes_content)
    prompt = (
        "Elite academic assistant. Follow instruction: '{user_prompt}'\n"
        "Format as beautiful Markdown. High-density.\n"
        f"COURSE NOTES:\n{full_context[:100000]}"
    )
    for model_id in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_id)
            response = model.generate_content(prompt)
            if response.text: return response.text
        except: continue
    return None

def generate_summary_filename(summary_text):
    prompt = f"Descriptive 2-4 word alphanumeric filename for this summary:\n{summary_text[:1000]}"
    for model_id in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_id)
            response = model.generate_content(prompt)
            if response.text: return sanitize(response.text.strip().replace(" ", "_"))
        except: continue
    return "Custom_Summary"

def summarize_category(course_name, category_name, summaries):
    combined = "\n".join([f"- {s}" for s in summaries])
    prompt = f"Summarize these topics for '{category_name or course_name}':\n{combined}\n\nProduce a 3-paragraph Markdown overview."
    for model_id in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_id)
            response = model.generate_content(prompt)
            if response.text: return response.text
        except: continue
    return None

def html_to_notes(url, course_name=None, category_hint=None, lec_hint=None, is_concise=False):
    """Fetch HTML, extract text from sections (Marp/Slides style), and generate notes."""
    try:
        print(f"    --- Fetching HTML slides from: {url}")
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Common slide containers: section, article, div.slide, div.remark-slide-container
        sections = soup.find_all(['section', 'article'])
        if not sections:
            # Fallback for generic pages if no sections found
            sections = [soup.find('main') or soup.find('body')]

        slide_texts = []
        for i, section in enumerate(sections):
            if not section: continue
            text = section.get_text(separator="\n", strip=True)
            if text:
                slide_texts.append(f"--- SLIDE {i+1} ---\n{text}")
        
        full_text = "\n\n".join(slide_texts)
        if len(full_text) < 100:
            print(f"      [!] HTML content too short, skipping.")
            return None

        print(f"    --- AI processing HTML slides ({len(full_text)} chars) ...")
        cat_instruction = f"### CATEGORY: '{category_hint}'.\n" if category_hint else ""
        lec_instruction = f"### LECTURE NUMBER: This is Lecture {lec_hint}.\n" if lec_hint else ""
        concise_instruction = (
            "### CONCISE MODE ACTIVE:\n"
            "- Generate compact study notes that preserve all core concepts and definitions.\n"
            "- DO NOT include worked examples, repeated intuition, long derivations, or implementation detail unless essential.\n"
            "- Compress each major topic into the minimum text needed for revision.\n"
            "- Prefer formulas, assumptions, conditions, and takeaways over narrative explanation.\n"
            "- The notes should feel like high-quality revision notes, not a transcript.\n"
        ) if is_concise else ""

        prompt = (
            f"You are a world-class professor creating ELITE Docusaurus notes from HTML slides.\n"
            f"COURSE: {course_name}\n"
            + cat_instruction + lec_instruction + concise_instruction +
            "## 1. YAML FRONT-MATTER RULES (STRICT):\n"
            "- EVERYTHING must be valid YAML.\n"
            "- ALL string values (especially 'course', 'title', 'lecture_name', 'category', 'summary') MUST be wrapped in double quotes (\").\n"
            "- Example: course: \"ES119 Principles of AI\"\n"
            "- 'sidebar_label': MUST be 'Lecture X'.\n"
            "- 'lecture_name': Descriptive human title.\n\n"
            "## 2. CONTENT RULES:\n"
            "- Focus 85% on theory. High density, concise.\n"
            "- Cover all major concepts from the source, but compress aggressively.\n"
            "- Prefer short, information-dense sections over long explanations.\n"
            "- Include only essential examples. Omit routine or repetitive examples.\n"
            "- Do not restate the same idea in multiple ways.\n"
            "- Convert slide bullet points into coherent academic prose and structured lists.\n"
            "- Use LaTeX for any formulas ($...$ for inline, $$...$$ for blocks).\n"
            "- MANDATORY: End with '## Quick Summary' section.\n"
            "KEYS: title, lecture_number, lecture_name, category, sidebar_label, sidebar_position, course, topic, tags, summary, math: true.\n\n"
            f"SLIDE CONTENT:\n{full_text[:30000]}" # Limit to 30k chars for safety
        )

        for model_id in MODELS_TO_TRY:
            try:
                model = genai.GenerativeModel(model_name=model_id)
                response = model.generate_content(prompt, request_options={"timeout": 600})
                if response.text:
                    text = response.text
                    if text.strip().startswith("```"):
                        text = re.sub(r'^```[a-zA-Z]*\n', '', text.strip())
                        text = re.sub(r'\n```$', '', text)
                    return fix_markdown_formatting(text)
            except: continue
    except Exception as e:
        print(f"      [!] HTML Processing Error: {e}")
    return None
