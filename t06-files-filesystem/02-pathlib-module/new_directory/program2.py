# ************************************* First Approach
# from pathlib import Path

# # # Create the directory
# docs_path = Path.cwd() / "documents"
# # docs_path.mkdir(exist_ok=True)  # Creates the subdirectory

# # # Populate the directory
# # for index, ext in enumerate(["png", "gif", "png", "jpg"], 1):
# #     file_path = docs_path / f"image{index}.{ext}"
# #     print(file_path)
# #     file_path.touch()
# #     print(file_path.exists())

# imgs_path = Path.cwd() / "images"
# imgs_path.mkdir(exist_ok=True)

# # Move the files to the new directory
# for file_path in docs_path.iterdir():
#     file_path.replace(str(file_path).replace("documents", "images"))


# ************************************* Second Approach
# # 12.4 Challenge: Move All Image Files To a New Directory
# # Solution to Challenge

# from pathlib import Path

# # Change this path to match the location on your computer
# documents_dir = Path.cwd() / "practice_files" / "documents"

# # Create an images/ directory in your home directory
# images_dir = Path.home() / "images"
# images_dir.mkdir(exist_ok=True)

# # Search for image files in the documents directory and move
# # them to the images/ directory
# for path in documents_dir.rglob("*.*"):
#     if path.suffix.lower() in [".png", ".jpg", ".gif"]:
#         path.replace(images_dir / path.name)
