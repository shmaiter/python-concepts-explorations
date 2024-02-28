from pathlib import Path

dirpath = Path.cwd() / "new_directory"

# ************************** ITERATING

# print(dirpath.iterdir())  # returns a "generator" <generator object Path.iterdir at 0x000001A9D7FE0430>
# print(list(dirpath.iterdir()))

# paths = [
#     dirpath / "program1.py",
#     dirpath / "program2.py",
#     dirpath / "dir_a" / "program3.py",
#     dirpath / "dir_a" / "dir_b" / "image1.jpg",
#     dirpath / "dir_a" / "dir_b" / "image2.png",
# ]

# for path in paths:
#     path.touch()

# print()
# for path in dirpath.iterdir():
#     print(path)

# ************************** SEARCHING
# print()
# print(list(dirpath.glob("*.py")))  # Matches any amount at the beginning, ending with ".py"
# print()
# print(list(dirpath.glob("*1*")))  # Matches any amount of chars in both sides of 1
# print()
# print(list(dirpath.glob("?ir_?")))  # Matches single char in both ends
# print()
# print(list(dirpath.glob("*1.??")))  # Matches any amount at start, containing "1." and ending with 2 chars(any)
# print()
# print(list(dirpath.glob("program[13].py")))  # Matches the word program, followed by either 1 or 3.
# print()
# print(list(dirpath.glob("**/*.txt")))  # Matches recursively, current and subdirectories with prefix "**/"
# print()
# print(list(dirpath.rglob("*.py")))  # Matches recursively, current and subdirectories with "rglob() method"


# ************************** RENAMING/MOVING
# source = dirpath / "dir_c"
# destination = dirpath / "dir_d"
# source.replace(destination)  # Moved to new location, overwrites if already exist, raises error if subdir doesn't exist

# file_path = dirpath / "program1.py"
# file_path.unlink()  # Deleting file

# pathlib doesn't has a recursive deleting on directories, so you'll need to delete all the
# files with in the dir and then the directory
# dir_d = dirpath / "dir_d"
# for path in dir_d.iterdir():
#     path.unlink()

# dir_d.rmdir()

# Or you can use another library, like shutil that comes built-in with python
# import shutil
# folder_a = dirpath / "dir_a"
# shutil.rmtree(folder_a)
