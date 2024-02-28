

with open('text.txt', 'r') as f:

    # --> reading the first amount of characters
    size_to_read = 10
    f_content4 = f.read(size_to_read)

    # --> tells the exact position of the cursor on the file being read
    # print(f.tell())

    # --> change the position from where you want to read
    # f.seek(0)  # return to the beginning

