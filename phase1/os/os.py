import os

# Get Current Working Directory
print(os.getcwd())

# Change Directory
print(os.chdir("/Users/adityasahu"))
print(os.getcwd())

# List files in a directory
files = os.listdir(".")
print(files)

# Make a Directory
os.mkdir("test_folder")

# Make nested directories
os.makedirs("parent/child/grandchild")

# Rename directory
os.rename("test_folder", "new_folder")

# Remove directory
os.rmdir("new_folder")
os.removedirs("parent/child/grandchild")



# check if a file or directory exits
os.path.exists("myfile.txt")

# File info
os.path.getsize("myfile.txt")
os.path.abspath("myfile.txt")

# Delete file
os.remove("myfile.txt")


# Get env variables
os.getenv("Home")

# Set an env variable
os.environ["MY_ENV"] = "12345"
os.getenv("MY_ENV")

# System commands (for automation, prefer the subprocess module (it’s safer))
os.system("ls") # linux/macos

# Path operations

# Join paths
path = os.path.join("User", "adityasahu", "Documents")
print(path)

# Split paths
os.path.basename("Users/adityasahu/notes.txt")
os.path.dirname("Users/adityasahu/notes.txt")

os.path.splitext("file.txt")
