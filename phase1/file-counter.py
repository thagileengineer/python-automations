import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Simple file counter")
parser.add_argument("path", help="folder path to count files.")
args = parser.parse_args()

path = Path(args.path)

print(path)

count = sum(1 for f in path.iterdir() if f.is_file())

print(f"{count} files found in {path}")
