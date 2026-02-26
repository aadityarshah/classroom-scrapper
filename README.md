# Classroom to Docusaurus: AI-Powered Lecture Notes

A modern, professional portal that automatically synchronizes your Google Classroom PDF materials, processes them using Gemini AI into concise, high-quality Markdown notes, and serves them via a sleek, monochrome Docusaurus site.

## ✨ Features

- **AI Note Generation**: Converts messy PDFs into structured, revision-ready Markdown.
- **$\LaTeX$ Support**: Beautifully rendered mathematical formulas via KaTeX.
- **Smart Categorization**: Automatically detects course sub-sections (e.g., Linear Algebra vs. Calculus).
- **Master Summaries**: Generates category-level "Big Picture" overviews using the `--summarize` flag.
- **Mobile Responsive**: Optimized for studying on-the-go with a premium glassmorphism design.
- **Instant Search**: Local search functionality across all synchronized notes.

---

## 🚀 Getting Started

### 1. Prerequisites

- **Node.js**: v18 or higher.
- **Python**: v3.10 or higher.
- **Google Cloud Account**: To access Classroom and Drive APIs.
- **Google AI Studio Key**: To access Gemini.

### 2. Setup Google Cloud (Classroom & Drive Access)

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project named `Classroom-Scrapper`.
3.  **Enable APIs**: Search for and enable the following:
    - **Google Classroom API**
    - **Google Drive API**
4.  **Configure OAuth Consent Screen**:
    - Choose "External" (or "Internal" if you have a Workspace).
    - Add the scope: `.../auth/classroom.courses.readonly`, `.../auth/classroom.courseworkmaterials.readonly`, `.../auth/classroom.topics.readonly`, and `.../auth/drive.readonly`.
5.  **Create Credentials**:
    - Go to **Credentials** > **Create Credentials** > **OAuth client ID**.
    - Select **Desktop App**.
    - Download the JSON file and rename it to `credentials.json` in the root of this repository.

### 3. Setup Gemini API

1.  Get an API Key from [Google AI Studio](https://aistudio.google.com/).
2.  Create a file named `api_key.py` in the root directory:
    ```python
    GEMINI_API_KEY = "your_actual_key_here"
    ```

### 4. Install Dependencies

```bash
# Install Python libraries
pip install -r requirements.txt

# Install Node.js dependencies
npm install --legacy-peer-deps
```

---

## 🛠️ Usage

### Synchronizing Notes

The sync script is highly flexible. It will download new PDFs, send them to Gemini, and save them to the `docs/` folder.

```bash
# Synchronize ALL configured courses (MA103, MA104)
python sync_classroom.py

# Synchronize ONLY a specific course
python sync_classroom.py --course "MA104"

# Update an existing note (overwrite)
python sync_classroom.py --filter "Lec 7" --force
```

### Generating Master Summaries

Build high-level overviews for specific categories:

```bash
# Summarize everything
python sync_classroom.py --summarize

# Summarize a specific category (e.g., Linear Algebra)
python sync_classroom.py --summarize --filter "Linear Algebra"
```

### Running the Website

```bash
npm run start
```
Your notes will be live at `http://localhost:3000`.

---

## 🎨 Personalization

- **Course Logic**: Edit `TARGET_IDS` in `sync_classroom.py` to add your own course codes.
- **Styling**: Modify `src/css/custom.css` to change the monochrome theme.
- **Logo**: Replace `static/img/logo.svg` with your own branding.

**Developed by Aaditya Rushabh Shah**
