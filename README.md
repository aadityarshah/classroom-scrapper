# Classroom to Docusaurus

Generate lecture notes from PDFs, Google Drive files, Google Classroom materials, or HTML slide pages, then publish them as a Docusaurus documentation site.

The repository has two main parts:

- Python scripts in `scripts/` that download source material and turn it into Markdown notes using Gemini.
- A Docusaurus site that serves the generated notes from `docs/`.

## What The Code Supports

- Sync notes from a public page that contains PDF links, HTML slide links, Google Drive links, SharePoint links, or OneDrive links.
- Process a direct PDF URL as input.
- Process a direct Google Drive file URL as input.
- Sync PDF attachments from Google Classroom.
- Prefer HTML slide pages over matching PDFs when both are present on a source page.
- Generate concise notes with `--concise`.
- Generate per-category summary pages with `--summarize`.
- Split a single Google Drive PDF into multiple lecture notes by page ranges with `scripts/generate_split_drive_notes.py`.

## Requirements

- Node.js 18+
- Python 3.10+
- A Gemini API key
- Google OAuth credentials if you want to use:
  - Google Classroom sync
  - Direct Google Drive file download
  - Google Drive links discovered during URL sync

## Setup

### 1. Clone and install

```bash
git clone https://github.com/aadityarshah/classroom-scrapper.git
cd classroom-to-gh-pages
pip install -r requirements.txt
npm install --legacy-peer-deps
```

### 2. Configure Gemini

Create `api_key.py` in the repo root:

```python
GEMINI_API_KEY = "your_actual_key_here"
```

### 3. Configure Google OAuth

This project uses OAuth to access Google Classroom and Google Drive through the Google APIs.

1. Create a project in Google Cloud Console.
2. Enable:
   - Google Classroom API
   - Google Drive API
3. Create an OAuth client for a desktop app.
4. Save the downloaded credentials file as `credentials.json` in the repo root.

On first run of a Google-backed script, the app opens an OAuth flow and stores the token in `token.pickle`.

## Quick Start

### Generate notes from a direct Google Drive PDF

```bash
python scripts/sync_url.py --url "https://drive.google.com/file/d/FILE_ID/view?usp=sharing" --course "ES119"
```

### Generate notes from a page that contains lecture links

```bash
python scripts/sync_url.py --url "https://example.com/course-page" --course "ES119"
```

### Generate concise notes only for one module

```bash
python scripts/sync_url.py --url "https://example.com/course-page" --course "ES119" --filter "Module 2" --concise
```

### Generate notes from Google Classroom

```bash
python scripts/sync_classroom.py --course "ES119"
```

### Split one Google Drive PDF into multiple lecture notes by page range

```bash
python scripts/generate_split_drive_notes.py --url "https://drive.google.com/file/d/FILE_ID/view?usp=sharing" --course "ES119" --module "Module 3" --ranges 1-24 25-56 --force
```

This creates a folder like `docs/ES119/Module 3/`, adds `_category_.json` if needed, splits the source PDF, and generates one note per range.

## CLI Reference

### `scripts/sync_url.py`

Use this when your source is:

- A webpage containing lecture material links
- A direct PDF URL
- A direct Google Drive file URL
- A direct HTML slide page

Command:

```bash
python scripts/sync_url.py --url "YOUR_URL" --course "COURSE_NAME" [FLAGS]
```

Flags:

- `--url`: Required. Source page URL, direct PDF URL, direct Google Drive file URL, or direct HTML slide URL.
- `--course`: Required. Output course folder under `docs/`.
- `--force`: Overwrite existing generated Markdown files.
- `--summarize`: Generate a `Summary.md` file for each category/module.
- `--concise`: Generate shorter summary-style notes instead of full notes.
- `--filter`: Only keep links whose inferred category or URL matches the provided substring.
- `--lecture`: Force a lecture number hint for the generated output.

Behavior notes:

- Direct Google Drive input is supported.
- If a source page contains both HTML slides and a matching PDF, the script prefers the HTML version.
- The script skips links that look like videos or notebooks.
- The script skips files whose filenames match blacklist terms such as assignments, quizzes, labs, and solutions.

Example:

```bash
python scripts/sync_url.py --url "https://drive.google.com/file/d/FILE_ID/view?usp=sharing" --course "ES119" --lecture 7 --force
```

### `scripts/sync_classroom.py`

Use this to pull PDF attachments from Google Classroom course materials.

Command:

```bash
python scripts/sync_classroom.py [FLAGS]
```

Flags:

- `--force`: Overwrite existing generated Markdown files.
- `--filter`: Only process files whose names contain the given substring.
- `--course`: Only process the course whose name or ID matches the substring.
- `--summarize`: Generate a `Summary.md` file for each category/module.

Behavior notes:

- The script currently only processes PDF drive attachments from course materials.
- By default it filters courses using the `TARGET_IDS` list inside `scripts/sync_classroom.py`.
- It uses Classroom topics as category folders.

Example:

```bash
python scripts/sync_classroom.py --course "MA104" --summarize
```

### `scripts/generate_split_drive_notes.py`

Use this when one PDF contains multiple lectures and you want separate notes for specific page ranges.

Command:

```bash
python scripts/generate_split_drive_notes.py --url "GOOGLE_DRIVE_FILE_URL" --course "COURSE_NAME" --module "MODULE_NAME" --ranges START-END START-END [--force]
```

Flags:

- `--url`: Required. Google Drive file URL.
- `--course`: Required. Course folder under `docs/`.
- `--module`: Required. Module/category folder name to write into.
- `--ranges`: Required. One or more page ranges like `1-24 25-56`.
- `--force`: Overwrite existing generated Markdown files.

Example:

```bash
python scripts/generate_split_drive_notes.py --url "https://drive.google.com/file/d/122VC1485T3EMt7HS1MBQDqM9D3jOg8b2/view?usp=sharing" --course "ES119" --module "Module 3" --ranges 1-24 25-56 --force
```

## Output Structure

Generated notes are written under `docs/`.

Typical structure:

```text
docs/
  ES119/
    _category_.json
    Module 1/
      Lec_01_....
    Module 2 Learning/
      Lec_01_....
    Module 3/
      _category_.json
      Lec_01_....
      Lec_02_....
```

The site uses the generated Markdown files directly, so after note generation you can start Docusaurus immediately.

## Running The Site

```bash
npm run start
```

Other commands:

- `npm run build`: Create a production build in `build/`
- `npm run serve`: Serve the built site locally
- `npm run clear`: Clear the Docusaurus cache

## How To Generate Your Own Notes

Choose the workflow based on your source:

1. If you have a page full of lecture links, use `scripts/sync_url.py`.
2. If you have a single Google Drive PDF, use `scripts/sync_url.py` for one note or `scripts/generate_split_drive_notes.py` for multiple notes from page ranges.
3. If your material lives in Google Classroom course materials, use `scripts/sync_classroom.py`.

Minimal examples:

```bash
python scripts/sync_url.py --url "https://example.com/my-course-page" --course "My Course"
python scripts/sync_url.py --url "https://drive.google.com/file/d/FILE_ID/view?usp=sharing" --course "My Course"
python scripts/generate_split_drive_notes.py --url "https://drive.google.com/file/d/FILE_ID/view?usp=sharing" --course "My Course" --module "Module 1" --ranges 1-20 21-42
python scripts/sync_classroom.py --course "My Course"
```

## Important Limitations

- Note quality depends on the quality and structure of the source PDF or HTML.
- The current Gemini integration uses `google.generativeai`, which is deprecated upstream but still works in this repo.
- `scripts/sync_classroom.py` currently targets course materials with PDF attachments, not every possible Classroom attachment type.
- `scripts/generate_split_drive_notes.py` currently supports Google Drive URLs only, not arbitrary local PDFs or arbitrary HTTP PDF URLs.

## Project Layout

- `scripts/`: Downloading, splitting, sync, and AI note-generation logic.
- `docs/`: Generated Markdown notes consumed by Docusaurus.
- `src/`: Custom Docusaurus theme, styles, and client-side UI behavior.
- `static/`: Static assets.
- `docusaurus.config.mjs`: Site config.
- `sidebars.mjs`: Sidebar configuration.

## Notes

- The first Google-backed run may prompt for browser-based authentication.
- Existing files are preserved unless you pass `--force`.
- Generated category folders do not all get `_category_.json` automatically; the split-note helper does create one for the requested module.

Developed by Aaditya Rushabh Shah.
