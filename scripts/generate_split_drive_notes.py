import argparse
import json
import os
import tempfile
from glob import glob

from pypdf import PdfReader, PdfWriter

from sync_url import extract_drive_id, download_from_drive
from utils import (
    extract_lecture_metadata,
    generate_lecture_filename,
    get_google_services,
    pdf_to_notes,
    sanitize,
)


def split_pdf(source_pdf, start_page, end_page, output_pdf):
    reader = PdfReader(source_pdf)
    writer = PdfWriter()
    total_pages = len(reader.pages)

    if start_page < 1 or end_page > total_pages or start_page > end_page:
        raise ValueError(
            f"Invalid page range {start_page}-{end_page} for PDF with {total_pages} pages."
        )

    for page_index in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_index])

    with open(output_pdf, "wb") as handle:
        writer.write(handle)


def ensure_category_file(module_dir, module_name, position):
    category_path = os.path.join(module_dir, "_category_.json")
    if os.path.exists(category_path):
        return

    payload = {
        "label": module_name,
        "position": position,
        "link": {
            "type": "generated-index",
            "description": f"Lecture notes for {module_name}.",
        },
    }

    with open(category_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def save_markdown(module_dir, source_name, lecture_index, module_name, markdown_text, force):
    lecture_number, lecture_name, category = extract_lecture_metadata(markdown_text)
    lecture_number = lecture_number or str(lecture_index)
    lecture_name = lecture_name or f"{module_name} Lecture {lecture_index}"
    category = category or module_name

    output_name = generate_lecture_filename(source_name, lecture_number, lecture_name)
    output_path = os.path.join(module_dir, f"{output_name}.md")

    if force:
        prefix = f"Lec_{str(lecture_number).replace('.', '-').zfill(2)}_"
        for existing_path in glob(os.path.join(module_dir, f"{prefix}*.md")):
            if os.path.normcase(existing_path) != os.path.normcase(output_path):
                os.remove(existing_path)
                print(f"   [CLEAN] Removed old version: {existing_path}")

    if os.path.exists(output_path) and not force:
        print(f"   [SKIP] Exists: {output_path}")
        return output_path

    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(markdown_text)

    print(f"   [DONE] Saved: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Download a Google Drive PDF, split it by page ranges, and generate lecture notes."
    )
    parser.add_argument("--url", required=True, help="Google Drive file URL.")
    parser.add_argument("--course", required=True, help="Course folder under docs/.")
    parser.add_argument("--module", required=True, help="Module folder under docs/<course>.")
    parser.add_argument(
        "--ranges",
        nargs="+",
        required=True,
        help="Page ranges in start-end form, in output order. Example: 1-24 25-56",
    )
    parser.add_argument("--concise", action="store_true", help="Generate concise revision-style notes.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing notes.")
    args = parser.parse_args()

    drive_id = extract_drive_id(args.url)
    if not drive_id:
        raise ValueError("Could not extract a Google Drive file ID from the provided URL.")

    course_name = sanitize(args.course.replace("_", " "))
    module_name = sanitize(args.module)
    module_dir = os.path.join("docs", course_name, module_name)
    os.makedirs(module_dir, exist_ok=True)

    module_position = 3
    digits = "".join(ch for ch in module_name if ch.isdigit())
    if digits:
        module_position = int(digits)
    ensure_category_file(module_dir, module_name, module_position)

    _, drive_service = get_google_services()

    with tempfile.TemporaryDirectory() as temp_dir:
        source_pdf = os.path.join(temp_dir, "source.pdf")
        success, original_filename = download_from_drive(drive_service, drive_id, source_pdf)
        if not success:
            raise RuntimeError("Failed to download PDF from Google Drive.")

        print(f"   [INFO] Downloaded: {original_filename}")

        for lecture_index, page_range in enumerate(args.ranges, start=1):
            start_page_str, end_page_str = page_range.split("-", 1)
            start_page = int(start_page_str)
            end_page = int(end_page_str)

            split_name = f"lecture_{lecture_index}_{start_page}_{end_page}.pdf"
            split_path = os.path.join(temp_dir, split_name)
            split_pdf(source_pdf, start_page, end_page, split_path)
            print(f"   [INFO] Split lecture {lecture_index}: pages {start_page}-{end_page}")

            markdown = pdf_to_notes(
                split_path,
                split_name,
                is_math=("MA" in course_name.upper() or "ES" in course_name.upper()),
                course_name=course_name,
                category_hint=module_name,
                lec_hint=str(lecture_index),
                is_concise=args.concise,
            )
            if not markdown:
                raise RuntimeError(
                    f"Failed to generate markdown for lecture {lecture_index} ({page_range})."
                )

            save_markdown(module_dir, split_name, lecture_index, module_name, markdown, args.force)


if __name__ == "__main__":
    main()
