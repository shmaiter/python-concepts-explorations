import os

# current directory of this python file
# print(os.getcwd())

# change directory
# os.chdir('D:\SoftDev\Python')

# list the directories
# print(os.listdir())

# creates a single directory
# os.mkdir('OS_demo')

# removes a single directory
# os.rmdir('D:\SoftDev\Python\Text_Formatting')

# creates intermediate directories when going levels down
# os.makedirs('OS_demo\sub_demo')

# removes intermediate directories when going levels down
# os.removedirs('OS_demo\sub_demo')

# renaming files
# os.rename('Python.pptx', 'Python_Elev8.pptx')

# seeing file details
# mode_time = os.stat('Python_Elev8.pptx').st_mtime
# print("Last modified:", datetime.fromtimestamp(mode_time))
#
# created_time = os.stat('Python_Elev8.pptx').st_atime
# print("Last accessed:", datetime.fromtimestamp(created_time))

# shows all nested directories and files under the specified path
# for dirpath, dirnames, files in os.walk(os.getcwd()):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', files)
#     print()

# available environment variables
# paths = os.environ.get("PATH").split(';')
# for path in paths:
#     print(path)

# directory and filenames extraction from a hole path
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))

# for join path without worrying about slashes
# print(os.path.join(os.getcwd(), 'test.txt'))

# Return True if path refers to an existing path or an open file descriptor
print(os.path.exists('/tmp/test.txt'))

# Return True if it's a directory
print(os.path.isdir(os.getcwd()))
# Return True if it's a file
print(os.path.isfile('/tmp/test.txt'))

# extract separately the path to the file and the extension
print(os.path.splitext('/tmp/test.txt'))

# Return a normalized absolutized version of the pathname path
current_file_path = os.path.abspath(__file__)
print(f"Current file path: {current_file_path}")
