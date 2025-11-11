from pathlib import Path


# Create path
path = Path('/Users/adityasahu/Documents')

# CWD
Path.cwd()

# Home directory
Path.home()

# Relative path
notesFile = Path("notes.txt")
Path.resolve(notesFile)

# Joining and navigating paths
docs = Path.home() / "Documents" / "notes.txt"

path.name
path.stem
path.suffix
path.parent
path.parents[1]

# Checking and creating files/folders
path2 = Path("Users/adityasahu/Downloads")
path2.exists()
path2.is_dir()
path2.is_file()


# Make directory
organized_dir = path2 / "organized"
organized_dir.mkdir(exist_ok=True)


# Make nested directories
(organized_dir / "images").mkdir(parents=True, exist_ok=True)

# List all files/folders
downloads = Path("Users/adityasahu/Downloads")

for item in downloads.iterdir():
    print(item)

# Filter files
for item in downloads.glob(".pdf"):
    print(item)

# Recursive search
for item in downloads.rglob(".png"):
    print(item)


# 5. File Operations

# Rename or remove
file = Path("Users/aditya/Downloads/screenshot.png")
file.rename("Users/aditya/Downloads/screenshot2.png")
file.unlink()

# Read and write text
text_file = Path("example.txt")
text_file.write_text("Hello, Python")
text_file.read_text()

# 6. File Information

file = Path("Users/aditya/Downloads/screenshot.png")
file_size = file.stat().st_size
last_modified = file.stat().st_mtime



# 7. Combining With Other Libraries

import shutil

source = Path.home() / "Downloads/file.zip"
dest = Path.home() / "Backups"

dest.mkdir(exist_ok=True)

shutil.move(str(source), dest)