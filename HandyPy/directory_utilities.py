"""
directory_utilities.py

Menu-driven utility script to:
1. Generate a directory chart
2. Copy only files from a directory
3. Create a blank folder-file structure

Author: Yug Agarwal
"""

import os
import shutil
from datetime import datetime

# ======================
# UTILITY FUNCTIONS
# ======================

def convert_size(size_bytes):
    """
    Converts bytes to best unit (B, KB, MB) with .2f formatting.
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes/1024:.2f} KB"
    else:
        return f"{size_bytes/(1024**2):.2f} MB"

def safe_copy(src, dest):
    """
    Copies file from src to dest.
    If dest file exists, appends _1, _2, etc. to filename.
    """
    base, extension = os.path.splitext(dest)
    counter = 1
    while os.path.exists(dest):
        dest = f"{base}_{counter}{extension}"
        counter += 1
    shutil.copy2(src, dest)

def get_valid_path(prompt, must_exist=True):
    """
    Prompts user for a path and validates it.
    If must_exist is True, ensures the path exists.
    """
    while True:
        path = input(prompt).strip('"').strip("'")
        path = os.path.abspath(path)
        if must_exist and not os.path.exists(path):
            print(f"❌ Path does not exist: {path}\nPlease enter a valid path.")
        else:
            return path

def get_extensions_input():
    """
    Prompts user to enter comma-separated list of extensions to exclude.
    Returns as a list of lowercase extensions with leading dots.
    """
    exts = input("Enter file extensions to exclude (comma separated, e.g. .ini,.log) or leave blank for none:\n> ")
    if not exts.strip():
        return []
    return [ext.strip().lower() for ext in exts.split(",")]

# ======================
# MAIN FUNCTIONS
# ======================

def generate_directory_chart(src_dir, chart_file, exclude_ext):
    """
    Generates a directory chart with file sizes and saves as Markdown file.
    Includes a timestamp of when the chart was created.
    """

    def recurse(path, prefix=""):
        entries = sorted(os.listdir(path))
        for index, entry in enumerate(entries):
            full_path = os.path.join(path, entry)
            connector = "└── " if index == len(entries) - 1 else "├── "
            if os.path.isdir(full_path):
                chart_lines.append(f"{prefix}{connector}{entry}/")
                extension = "    " if index == len(entries) - 1 else "│   "
                recurse(full_path, prefix + extension)
            else:
                size = convert_size(os.path.getsize(full_path))
                exclude_note = " [Excluded]" if any(entry.lower().endswith(ext) for ext in exclude_ext) else ""
                chart_lines.append(f"{prefix}{connector}{entry} ({size}){exclude_note}")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chart_lines = [f"# Directory Chart", f"Generated on: {timestamp}", "", f"{os.path.basename(src_dir)}/"]
    recurse(src_dir)

    with open(chart_file, "w", encoding="utf-8") as f:
        f.write("\n".join(chart_lines))
    print(f"\n✅ Directory chart saved to: {chart_file}")

def copy_files_only(src_dir, dest_dir, exclude_ext):
    """
    Recursively copies only files (not folders) to dest_dir.
    Excludes files with extensions in exclude_ext.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in exclude_ext):
                print(f"Excluded from copy: {file}")
                continue
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_dir, file)
            safe_copy(src_file_path, dest_file_path)
            print(f"Copied: {src_file_path} -> {dest_file_path}")

def create_blank_structure(src_dir, dest_dir):
    """
    Recreates the folder and file structure of src_dir in dest_dir with empty files.
    Includes excluded files as well for structural representation.
    """
    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        current_dest_dir = os.path.join(dest_dir, rel_path)
        os.makedirs(current_dest_dir, exist_ok=True)
        for file in files:
            dest_file_path = os.path.join(current_dest_dir, file)
            with open(dest_file_path, "w", encoding="utf-8") as f:
                pass
            print(f"Created empty file: {dest_file_path}")

# ======================
# MENU LOOP
# ======================

if __name__ == "__main__":
    print("\n📁 Directory Utilities Menu\n")

    while True:
        print("\nChoose an option:")
        print("1. Generate Directory Chart")
        print("2. Copy Files Only")
        print("3. Create Blank Structure")
        print("4. Exit")

        choice = input("> ").strip()

        if choice == "1":
            src = get_valid_path("Enter source directory path:\n> ")
            chart = input("Enter output chart file path (will create/overwrite .md file):\n> ").strip('"').strip("'")
            chart = os.path.abspath(chart)
            exclude = get_extensions_input()
            generate_directory_chart(src, chart, exclude)

        elif choice == "2":
            src = get_valid_path("Enter source directory path:\n> ")
            dest = get_valid_path("Enter destination directory path for files only:\n> ", must_exist=False)
            exclude = get_extensions_input()
            copy_files_only(src, dest, exclude)

        elif choice == "3":
            src = get_valid_path("Enter source directory path:\n> ")
            dest = get_valid_path("Enter destination directory path for blank structure:\n> ", must_exist=False)
            create_blank_structure(src, dest)

        elif choice == "4":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
