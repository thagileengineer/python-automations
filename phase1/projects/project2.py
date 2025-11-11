# Move all .jpg files from Downloads to Pictures.
from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"
pictures = downloads / "Pictures"
pictures.mkdir(exist_ok=True)

for f in downloads.glob("*.HEIC"):
    shutil.move(str(f), pictures)
