
# 'w' flag creates the file if it doesn't exist, or overwrite it if exist
# 'a' is for append to the end.
with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)