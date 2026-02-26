# classroom-scrapper

This repository contains `sync_classroom.py` which downloads PDFs from Google Classroom, sends them to Gemini to generate structured Markdown notes, and saves them under `docs/`.

We scaffolded a minimal Docusaurus site to present the generated notes with math support (KaTeX).

Quick start:

1. Install Node.js (v16+ recommended) and Python dependencies.

2. Install Docusaurus dependencies:

```bash
npm install
```

3. Run locally:

```bash
npm run start
```

4. Edit `api_key.py` and set `GEMINI_API_KEY`.

5. Run the sync script:

```bash
python sync_classroom.py
```

The script will write Markdown files into `docs/` that Docusaurus serves.
