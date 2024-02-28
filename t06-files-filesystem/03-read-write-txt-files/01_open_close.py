f = open("text.txt", "r")

# name of your text file
print(f.name)

# the mode in which your working with the file
print(f.mode)

# print the content
for i in f:
    print(i)

f.close()