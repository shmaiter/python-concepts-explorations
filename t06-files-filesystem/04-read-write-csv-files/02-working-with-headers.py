from pathlib import Path
import csv
import re

people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24},
]


def process_row(row):
    row["salary"] = float(row["salary"])


def is_float(s):
    return re.match(r"^\d+(.\d+)$", s) is not None


# *********************************************** 2nd APPROACH -> WRITING
file_path = Path.cwd() / "people.csv"
with file_path.open(mode="w", encoding="utf-8", newline="\n") as file:
    writer = csv.DictWriter(file, fieldnames=people[0].keys())
    writer.writeheader()
    writer.writerows(people)


# *********************************************** 1st APPROACH -> WRITING
# file_path = Path.cwd() / "people.csv"
# file = file_path.open(mode="w", encoding="utf-8", newline="\n")
# writer = csv.DictWriter(file, fieldnames=people[0].keys())
# writer.writeheader()
# writer.writerows(people)
# file.close()

# *********************************************** 2nd APPROACH -> READING
# file_path = Path.cwd() / "employees.csv"
# with file_path.open(mode="r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         process_row(row)
#         print(row)


# *********************************************** 1st APPROACH -> READING
# file_path = Path.cwd() / "employees.csv"
# file = file_path.open(mode="r", encoding="utf-8")
# reader = csv.DictReader(file)

# # print(reader.fieldnames)  # returns a list with the headers
# for row in reader:
#     print(row)
#     # returns
#     # {"name": "Lee", "department": "Operations", "salary": "75000.00"}
#     # {"name": "Jane", "department": "Engineering", "salary": "85000.00"}
#     # {"name": "Diego", "department": "Sales", "salary": "80000.00"}

# file.close()
