import pathlib

# user 'r' letter before strings to avoid escape sequences
string_path = pathlib.Path(r"C:\Users\shmai")

# The object created with 'Path' is a subclass called 'WindowsPath' on linux will be 'PosixPath'.
print(type(string_path))

print(pathlib.Path.cwd())

# Concatenating paths
home = pathlib.Path.home()
filepath = home / r"OneDrive\Escritorio\hello.txt"
# "C:\Users\shmai\OneDrive\Escritorio\hello.txt"
print(filepath)

# List of nested parent directories recursively to the root
print(list(filepath.parents))

for directory in filepath.parents:
    print(directory)

# Returns only the first parent up from the path
print(filepath.parent)

# If the filepath is ABSOLUTE you can access the root
print(filepath.anchor)  # Returns a "string" not a "WindowsPath" object

# print(dir(filepath))

# The .name attribute returns the name of the file or directory that the path points to:
print(home.name)
print(filepath.name)

# The name of a file is broken down into two parts. The part to the left of the dot (.) is called the stem,
# and the part to the right of the dot (.) is called the sufix or file extension.
print(filepath.stem)
print(filepath.suffix)

# File exists in your machine
print(filepath.exists())

# You can check whether or not a file path refers to a file or a directory
# returns False if the file doesn't exist.
print(filepath.is_file())

# The same happens with directories
print(filepath.is_dir())

