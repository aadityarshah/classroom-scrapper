import os
import sys
import time
import io
import re
import yaml
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from googleapiclient.http import MediaIoBaseDownload

# Import from utils
from utils import (
    sanitize, pdf_to_notes, extract_lecture_metadata, 
    generate_lecture_filename, summarize_category, BLACKLIST,
    get_google_services, analyze_page_structure, html_to_notes
)

def extract_drive_id(url):
    patterns = [
        r'drive\.google\.com/file/d/([a-zA-Z0-9_-]+)',
        r'drive\.google\.com/open\?id=([a-zA-Z0-9_-]+)',
        r'docs\.google\.com/file/d/([a-zA-Z0-9_-]+)',
        r'drive\.google\.com/uc\?id=([a-zA-Z0-9_-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match: return match.group(1)
    return None

def handle_onedrive_link(url):
    if "sharepoint.com" in url or "onedrive.live.com" in url:
        if "download=1" not in url:
            separator = "&" if "?" in url else "?"
            return f"{url}{separator}download=1"
    return url

def download_from_drive(drive_service, file_id, output_path):
    try:
        request = drive_service.files().get_media(fileId=file_id)
        file_metadata = drive_service.files().get(fileId=file_id).execute()
        filename = file_metadata.get('name', 'file.pdf')
        with io.FileIO(output_path, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request, chunksize=1024*1024)
            done = False
            while not done: _, done = downloader.next_chunk()
        return True, filename
    except Exception as e:
        print(f"      [!] Drive Download Error: {e}")
        return False, None

def download_direct(url, output_path, retries=3):
    url = handle_onedrive_link(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    for attempt in range(retries):
        try:
            response = requests.get(url, stream=True, timeout=45, headers=headers, allow_redirects=True)
            response.raise_for_status()
            if 'html' in response.headers.get('content-type', '').lower(): return False, None
            
            filename = "file.pdf"
            cd = response.headers.get('content-disposition')
            if cd:
                fname_match = re.findall('filename[^;=\n]*=(([\'"]).*?\\2|[^;\n]*)', cd)
                if fname_match: filename = fname_match[0][0].strip('"').strip("'")
            else:
                filename = os.path.basename(urlparse(url).path) or "file.pdf"
                if not filename.lower().endswith(".pdf"): filename += ".pdf"

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192): f.write(chunk)
            return True, filename
        except:
            if attempt < retries - 1: time.sleep(5 * (attempt + 1))
            else: return False, None
    return False, None

def main():
    parser = argparse.ArgumentParser(description='Sync PDFs from any URL to Docusaurus.')
    parser.add_argument('--url', type=str, required=True, help='URL of the page.')
    parser.add_argument('--course', type=str, required=True, help='Course name (e.g., MA104).')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files.')
    parser.add_argument('--summarize', action='store_true', help='Generate Master Summaries.')
    parser.add_argument('--concise', action='store_true', help='Generate concise notes (summary style).')
    parser.add_argument('--filter', type=str, help='Filter for specific category/module (e.g., "Module 2").')
    args = parser.parse_args()

    _, drive = get_google_services()
    course_clean = sanitize(args.course.replace("_", " "))
    print(f"\n>> Synchronizing: {course_clean} from {args.url}")

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(args.url, timeout=30, headers=headers)
        response.raise_for_status()

        is_pdf_direct = 'application/pdf' in response.headers.get('content-type', '').lower() or args.url.lower().endswith('.pdf')
        # Only treat as direct HTML note if it's explicitly an .html file and NOT a known course contents/index page
        is_html_direct = ('text/html' in response.headers.get('content-type', '').lower() and 
                          (args.url.lower().endswith('.html') or args.url.lower().endswith('.htm')) and 
                          not any(k in args.url.lower() for k in ['course-contents', 'index', 'schedule']))
        
        print(f"   [DEBUG] is_pdf_direct: {is_pdf_direct}, is_html_direct: {is_html_direct}", flush=True)
        
        pdf_links = []
        html_links = []
        url_to_category = {}

        if is_pdf_direct:
            pdf_links.append({'type': 'direct', 'url': args.url, 'orig_href': args.url})
        elif is_html_direct:
            html_links.append({'url': args.url, 'orig_href': args.url})
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Pass the soup object for deep structural analysis
            url_to_category = analyze_page_structure(soup, args.url, course_clean)
            print(f"   [DEBUG] Category mapping found for {len(url_to_category)} URLs", flush=True)
            
            for link in soup.find_all('a'):
                href = link.get('href')
                if not href: continue
                abs_url = urljoin(args.url, href)
                print(f"   [DEBUG] Found raw URL: {abs_url}", flush=True)

                # Skip Colab/Notebook/Video links as requested by user
                if any(k in abs_url.lower() for k in ['colab', 'notebook', 'youtube', 'vimeo', 'video']):
                    continue

                drive_id = extract_drive_id(abs_url)
                if drive_id: pdf_links.append({'type': 'drive', 'id': drive_id, 'url': abs_url, 'orig_href': href})
                elif ".pdf" in abs_url.lower() or "sharepoint.com" in abs_url or "onedrive.live.com" in abs_url:
                    pdf_links.append({'type': 'direct', 'url': abs_url, 'orig_href': href})
                elif ".html" in abs_url.lower() or ".htm" in abs_url.lower():
                    # Relaxed filter for HTML links
                    if any(k in abs_url.lower() for k in ['note', 'slide', 'lecture', 'lec', 'foundation', 'regression', 'neural', 'module', 'learning']):
                        html_links.append({'url': abs_url, 'orig_href': href})

        # --- ALGORITHM: HTML-over-PDF Prioritization ---
        seen_pdf = set()
        unique_pdf = [l for l in pdf_links if l['url'] not in seen_pdf and not seen_pdf.add(l['url'])]
        
        seen_html = set()
        unique_html = [l for l in html_links if l['url'] not in seen_html and not seen_html.add(l['url'])]
        
        print(f"   [DEBUG] Unique PDFs: {len(unique_pdf)}, Unique HTMLs: {len(unique_html)}", flush=True)
        
        final_links = []
        html_used = set()
        
        for p in unique_pdf:
            pdf_base = os.path.splitext(os.path.basename(urlparse(p['url']).path))[0].lower()
            matching_html = None
            for h in unique_html:
                html_base = os.path.splitext(os.path.basename(urlparse(h['url']).path))[0].lower()
                if pdf_base == html_base or pdf_base in html_base or html_base in pdf_base:
                    matching_html = h
                    break
            
            if matching_html:
                print(f"   [FOUND] HTML alternative for {pdf_base}.pdf -> {matching_html['url']}")
                matching_html['is_html'] = True
                final_links.append(matching_html)
                html_used.add(matching_html['url'])
            else:
                p['is_html'] = False
                final_links.append(p)
        
        # Add remaining HTML links that likely contain slides
        for h in unique_html:
            if h['url'] not in html_used:
                h['is_html'] = True
                final_links.append(h)

        print(f"   Found {len(final_links)} unique potential links.")
        
        all_summaries = {}
        for link_data in final_links:
            url = link_data['url']
            
            # Lookup pre-analyzed category using both absolute and relative URLs
            cat_hint = url_to_category.get(url) or url_to_category.get(link_data['orig_href']) or ""
            
            # FILTER: If filter is provided, skip if category doesn't match
            if args.filter and args.filter.lower() not in cat_hint.lower():
                # Double check the URL/Title if category hint is empty or doesn't match
                if args.filter.lower() not in url.lower():
                    continue

            print(f"   Processing: {url} (Category: {cat_hint})")
            
            md_text = None
            original_filename = "file.pdf"

            if link_data.get('is_html'):
                md_text = html_to_notes(url, course_name=course_clean, category_hint=cat_hint, lec_hint=None, is_concise=args.concise)
                original_filename = os.path.basename(urlparse(url).path)
            else:
                temp_pdf = "temp_url.pdf"
                success, original_filename = (download_from_drive(drive, link_data['id'], temp_pdf) if link_data['type'] == 'drive' else download_direct(url, temp_pdf))
                print(f"      Download success: {success}, filename: {original_filename}")
                
                if not success or not original_filename or any(word in original_filename.lower() for word in BLACKLIST): 
                    if original_filename and any(word in original_filename.lower() for word in BLACKLIST):
                        print(f"      [SKIP] Blacklisted: {original_filename}")
                    continue
                
                # Try to extract lecture number hint from filename or URL
                lec_hint = None
                match = re.search(r'(?:Lec|Lecture|svc|Unit)\D*(\d+)', url, re.IGNORECASE)
                if not match:
                    match = re.search(r'(?:Lec|Lecture|svc|Unit)\D*(\d+)', original_filename, re.IGNORECASE)
                if match: lec_hint = match.group(1)

                md_text = pdf_to_notes(temp_pdf, original_filename, is_math=("MA" in course_clean.upper() or "ES" in course_clean.upper()), 
                                    course_name=course_clean, category_hint=cat_hint, lec_hint=lec_hint, is_concise=args.concise)
            
            if md_text:
                for seg in md_text.split("<!-- LECTURE_SPLIT -->"):
                    seg = seg.strip()
                    if not seg: continue
                    lec_num, lec_name, category = extract_lecture_metadata(seg)
                    
                    category = category or cat_hint # AI output or Structural Analysis fallback

                    # Final safety filter check on the extracted category
                    if args.filter and args.filter.lower() not in (category or "").lower():
                        continue

                    if args.summarize:
                        fm_match = re.search(r'---\s*(.*?)\s*---', seg, re.DOTALL)
                        if fm_match:
                            try:
                                fm = yaml.safe_load(fm_match.group(1))
                                if fm and fm.get('summary'):
                                    key = (course_clean, category)
                                    if key not in all_summaries: all_summaries[key] = []
                                    all_summaries[key].append(fm.get('summary'))
                            except Exception as ye:
                                print(f"      [!] YAML Error in segment: {ye}")

                    out_dir = os.path.join("docs", course_clean, sanitize(category)) if category else os.path.join("docs", course_clean)
                    os.makedirs(out_dir, exist_ok=True)

                    filename = generate_lecture_filename(original_filename, lec_num, lec_name)
                    out_file = os.path.join(out_dir, f"{filename}.md")
                    if os.path.exists(out_file) and not args.force: continue
                        
                    with open(out_file, "w", encoding="utf-8") as f: f.write(seg)
                    print(f"   [DONE] Saved: {filename}.md in {category if category else 'root'}")
            time.sleep(3)

        if args.summarize:
            for (course, category), summaries in all_summaries.items():
                master_md = summarize_category(course, category, summaries)
                if master_md:
                    out_path = os.path.join("docs", sanitize(course), sanitize(category), "Summary.md") if category else os.path.join("docs", sanitize(course), "Summary.md")
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    final_text = f"---\ntitle: |\n  Summary: {category or course}\nsidebar_label: Summary\nsidebar_position: 0\n---\n\n{master_md}"
                    with open(out_path, "w", encoding="utf-8") as f: f.write(final_text)
    except Exception as e: print(f"   Error: {e}")

if __name__ == "__main__": main()
