import os

downloads = "/Users/adityasahu/Downloads"
_100MB = 100 * 1024 * 1024

for file in os.listdir(downloads):
    path = os.path.join(downloads, file)
    if os.path.isfile(path=path):
        size = os.path.getsize(path)
        
        if size > _100MB:
            print(f"large file {file} ({size/1024/1024:.2f} MB)")