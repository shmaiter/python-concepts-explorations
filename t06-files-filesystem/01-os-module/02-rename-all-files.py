import os


def modify_path(path: str) -> str:
    mod_path = repr(path).replace("'", "")
    mod_path = mod_path.replace('"', "")
    print(mod_path)
    return mod_path


dir_path = modify_path(input("Enter your path: \n > "))
# dir_path = r"F:\Sabikui Bisco"
files_list = sorted(os.listdir(dir_path))
print(f"\nCurrent directory filenames: \n{files_list}")

for i, file in enumerate(files_list, 1):
    current_full_path = os.path.join(dir_path, file)
    current_filename = file.split(".")[0]
    new_full_path = current_full_path.replace(str(current_filename), str(i))
    os.rename(current_full_path, new_full_path)

print("\nFinished renaming!!")
files_list = sorted(os.listdir(dir_path))
print(f"\nNew directory filenames: \n{files_list}")
