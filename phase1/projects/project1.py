# List all .py files in your Documents folder
from pathlib import Path

downloads = Path.home() / "Downloads"
print(downloads)

for file in downloads.iterdir():
    if file.is_file():
        ext = file.suffix[1:]
        if ext == "py":
            print(file.name)