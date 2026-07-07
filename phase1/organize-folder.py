#!/usr/bin/env python3
import argparse
from pathlib import Path
import shutil
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory into subdirectories based on their file extensions."
    )
    parser.add_argument(
        "folder_path",
        type=str,
        help="The path to the folder to organize."
    )
    args = parser.parse_args()

    folder_path = Path(args.folder_path).resolve()

    if not folder_path.exists():
        print(f"Error: The path '{folder_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if not folder_path.is_dir():
        print(f"Error: The path '{folder_path}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    print(f"Organizing files in: {folder_path}")
    organized = folder_path / "organized"
    
    moved_count = 0

    try:
        organized.mkdir(exist_ok=True)
        script_path = Path(__file__).resolve()

        for file in folder_path.iterdir():
            # Skip directories, the target 'organized' folder itself, and this script if it's there
            if file.is_dir() or file.resolve() == organized.resolve() or file.resolve() == script_path:
                continue

            if file.is_file():
                ext = file.suffix[1:].lower() if file.suffix else "others"
                if not ext:
                    ext = "others"
                
                target_folder = organized / ext
                target_folder.mkdir(exist_ok=True)
                
                shutil.move(str(file), target_folder / file.name)
                moved_count += 1
                
        print(f"Success! Organized {moved_count} files into '{organized.relative_to(folder_path)}'.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
