# Classroom to Docusaurus: AI-Powered Lecture Notes

A modern, professional portal that automatically synchronizes your academic materials from Google Classroom or any web URL, processes them using Gemini AI into concise, high-quality Markdown notes, and serves them via a sleek, monochrome Docusaurus site.

---

## ✨ Key Features

- **Multi-Source Sync**: Fetch materials from Google Classroom or any public URL (Google Sites, SharePoint, etc.).
- **Smart HTML Detection**: Automatically prioritizes HTML-based slides (Marp/Reveal.js) over heavy PDFs for 10x faster generation.
- **AI Note Generation**: Converts messy slides into structured prose with definitions, theorems, and summaries.
- **$\LaTeX$ Support**: High-fidelity mathematical rendering via KaTeX, now **fully rendered in the Table of Contents (TOC)** and throughout the site.
- **Downloadable Notes**: **New!** Download any lecture note as a clean `.md` file or save it as a professionally formatted `.pdf`.
- **Concise Mode**: **New!** Generate high-level summaries focusing on core concepts and logic for quick 2-3 minute reads.
- **Auto-Scrolling TOC**: The right sidebar automatically follows your reading position.
- **Mobile Optimized**: Premium glassmorphism design with a fully functional mobile sidebar for study sessions on any device.

---

## 🚀 Local Setup & Installation

### 1. Prerequisites
- **Node.js**: v18.0.0 or higher
- **Python**: v3.10.0 or higher
- **Gemini API Key**: Obtain from [Google AI Studio](https://aistudio.google.com/)

### 2. Repository Setup
```bash
# Clone the repository
git clone https://github.com/aadityarshah/classroom-scrapper.git
cd classroom-to-gh-pages

# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies
npm install --legacy-peer-deps
```

### 3. Configuration
1. **API Key**: Create `api_key.py` in the root directory:
   ```python
   GEMINI_API_KEY = "your_actual_key_here"
   ```
2. **Google Cloud (Optional for Classroom Sync)**: 
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/).
   - Enable **Google Classroom API** and **Google Drive API**.
   - Download the OAuth Client ID JSON and save it as `credentials.json` in the root.

---

## 🛠️ CLI Reference (Synchronizing Content)

All synchronization scripts are located in the `scripts/` directory.

### A. Syncing from a URL (e.g. Google Sites)
Use this when your course materials are hosted on a public website.
```bash
python scripts/sync_url.py --url "YOUR_URL" --course "COURSE_NAME" [FLAGS]
```
**Available Flags:**
- `--url`: (Required) The page containing PDF or HTML links.
- `--course`: (Required) Folder name in `docs/` (e.g., ES119).
- `--concise`: **New!** Generates concise, summary-style notes instead of full lecture notes.
- `--filter`: **New!** Filter for specific categories or modules (e.g., `--filter "Module 2"`).
- `--summarize`: Generates a "Summary.md" for each category based on AI insights.
- `--force`: Overwrites existing files even if they haven't changed.

### B. Syncing from Google Classroom
Use this for officially enrolled courses.
```bash
# Sync all courses defined in TARGET_IDS within the script
python scripts/sync_classroom.py

# Sync a specific course only
python scripts/sync_classroom.py --course "MA104"
```

---

## 💻 Running the Website

Once the notes are generated in the `docs/` folder, start the site:

| Command | Description |
| :--- | :--- |
| `npm run start` | Starts a local development server at `http://localhost:3000` |
| `npm run build` | Bundles the site into static files for production (in `build/`) |
| `npm run serve` | Serves the production build locally |
| `npm run clear` | Clears the Docusaurus cache |

---

## 🎨 Customization

- **Add New Courses**: Run `sync_url.py` with a new course name; the sidebar will update automatically.
- **Change Aesthetics**: Modify `src/css/custom.css` to adjust colors, fonts, or glassmorphism intensity.
- **Home Page**: Edit `docs/index.mdx` to update the cards and welcome message.
- **Site Config**: Edit `docusaurus.config.mjs` to change the site title, navbar links, or organization name.

---

## 📁 Project Structure

- `scripts/`: Python logic for scraping, downloading, and AI processing.
- `docs/`: The generated Markdown notes (categorized by course).
- `src/`: Custom CSS, JavaScript (TOC scroll & LaTeX rendering), and theme swizzles.
- `static/`: Images, logos, and static assets.

**Developed by Aaditya Rushabh Shah**
