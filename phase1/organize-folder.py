from pathlib import Path
import shutil

folderPath = Path.home() / "Downloads"

organized = folderPath / "organized"

organized.mkdir(exist_ok=True)

for file in folderPath.iterdir():
    if file.is_file():
        ext = file.suffix[1:] or "others"
        target_folder = organized / ext
        target_folder.mkdir(exist_ok=True)
        shutil.move(str(file), target_folder/ file.name)
