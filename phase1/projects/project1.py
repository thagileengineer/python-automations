# List all .py files in your Documents folder
from pathlib import Path

downloads = Path.home() / "Downloads"
print(downloads)

for file in downloads.glob("*.py"):
    print(file.name)