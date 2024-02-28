from pathlib import Path

# Creating a directory
new_dir = Path.cwd() / "new_directory"
print("\nThe directory exist and is a directory")
print(new_dir.exists())
print(new_dir.is_dir())
# new_dir.mkdir()  # Raises an error if already exists
new_dir.mkdir(exist_ok=True)  # Doesn't raise an error if already exists

# Creating nested directories
nested_dir = new_dir / "dir_a" / "dir_b"
# nested_dir.mkdir()  # Raises an error if subdirectory "dir_a" doesn't exist
nested_dir.mkdir(parents=True, exist_ok=True)  # Common pattern for creating directories
# if the path is input by a user, you may wish to instead catch
# an exception so that you can ask the user to verify that the path they
# entered is correct

# Creating files
filepath = new_dir / "file1.txt"
# For creating a file
filepath.touch()
print("\nThe file exist and is a file")
print(filepath.exists())
print(filepath.is_file())

# Creating file without the intermediate directory
filepath = new_dir / "dir_c" / "file2.txt"
# filepath.touch()  # Raises an exception because the subdir "dir_c" doesn't exist
# Instead used the following technique
filepath.parent.mkdir()
filepath.touch()

