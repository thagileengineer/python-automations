# Create a script that prints file sizes in a folder in descending order.

from pathlib import Path

documents = Path.home() / "Documents"
files = []

for f in documents.iterdir():
    if f.is_file():
        files.append({
            "name": f.name,
            "size": f.stat().st_size
        })

files.sort(key=lambda f: f["size"], reverse=True)

for item in files:
    print(item["size"], item["name"])
