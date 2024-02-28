from pathlib import Path
import csv

# ********************************************************** Exercise #1 **********************************************************
# Write a script that writes the following list of lists to a file called
# numbers.csv in your home directory:

# numbers = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
# ]

# file_path = Path.cwd() / "numbers.csv"
# with file_path.open(mode="w", encoding="utf-8", newline="\n") as file:
#     writer = csv.writer(file)
#     writer.writerows(numbers)

# ********************************************************** Exercise #2 **********************************************************
# Write a script that reads the numbers in the numbers.csv file from
# Exercise 1 into a list of lists of integers called numbers. Print the list
# of lists. Your output should like the following:
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# file_path = Path.cwd() / "numbers.csv"
# with file_path.open(mode="r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     numbers = []
#     for row in reader:
#         if len(row) != 0:
#             processed_row = [int(num) for num in row]
#             numbers.append(processed_row)
#     print(numbers)

# ********************************************************** Exercise #3 **********************************************************
# Write a script that writes the following list of dictionaries to a file
# called favorite_colors.csv in your home directory:

# favorite_colors = [
#     {"name": "Joe", "favorite_color": "blue"},
#     {"name": "Anne", "favorite_color": "green"},
#     {"name": "Bailey", "favorite_color": "red"},
# ]

# file_path = Path.cwd() / "favorite_colors.csv"
# with file_path.open(mode="w", encoding="utf-8", newline="\n") as file:
#     writer = csv.DictWriter(file, favorite_colors[0].keys())
#     writer.writeheader()
#     writer.writerows(favorite_colors)

# ********************************************************** Exercise #4 **********************************************************
# Write a script that reads the data from the favorite_colors.csv file
# from Exercise 3 into a list of dictionaries called favorite_colors
# Print the list of dictionaries. The output should look something
# like this:
# [{"name": "Joe", "favorite_color": "blue"},
# {"name": "Anne", "favorite_color": "green"},
# {"name": "Bailey", "favorite_color": "red"}]

file_path = Path.cwd() / "favorite_colors.csv"
favorite_colors = []
with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors.append(row)
    print(favorite_colors)
