

with open('text.txt', 'r') as f:
    #  --> methods that come within the 'f'
    # f_contents1 = f.read()
    # print(type(f_contents1))
    #
    # f_contents2 = f.readlines()
    # print(type(f_contents2))
    #
    # f_contents3 = f.readline()
    # print(type(f_contents3))

    # --> extracting one line a the time, like with a generator
    # for line in f:
    #     print(line, end='')

    # --> reading the first amount of characters
    # size_to_read = 10
    # f_content4 = f.read(size_to_read)

    # --> tells the exact position of the cursor on the file being read
    print(f.tell())

    # --> change the position from where you want to read
    # f.seek(0)  # return to the beginning

    # --> extract the content in chunks
    # while len(f_content4) > 0:
    #     print(f_content4, end='*')
    #     f_content4 = f.read(size_to_read)

# print(f.name, f.mode)
