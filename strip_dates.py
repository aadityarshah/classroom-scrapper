import os
import re

def strip_dates(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") or file.endswith(".mdx"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    # Remove lines that start with 'date:' inside the front-matter
                    if not re.match(r'^date:\s*.*$', line):
                        new_lines.append(line)

                if len(lines) != len(new_lines):
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    print(f"Removed date from: {file_path}")

if __name__ == "__main__":
    strip_dates("docs")
    print("Done! Dates have been removed from all files.")
