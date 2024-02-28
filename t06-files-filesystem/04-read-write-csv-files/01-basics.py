from pathlib import Path
import csv

# daily_temperatures = [
#     [68, 65, 68, 70, 74, 72],
#     [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73],
# ]

daily_temperatures = []

# *********************************************** 1st APPROACH -> READING
# path = Path.cwd() / "temperatures.csv"
# file = path.open(mode="r", encoding="utf-8")
# reader = csv.reader(file)
# for row in reader:
#     print(row)
# file.close()

# *********************************************** 1st APPROACH -> READING
path = Path.cwd() / "temperatures.csv"
with path.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        daily_temperatures.append(int_row)

print(daily_temperatures)


# *********************************************** 1st APPROACH -> WRITING
# temperature_readings = [68, 65, 68, 70, 74, 72]
# path = Path.cwd() / "temperatures.csv"
# with path.open(mode="a", encoding="utf-8", newline="\n") as file:
#     file.write(str(temperature_readings[0]))  # Just append the first one

#     for temp in temperature_readings[1:]:
#         file.write(f",{temp}")  # Add each temperature one by one

# with path.open(mode="r", encoding="utf-8") as file:
#     text = file.read()
# print(text)

# *********************************************** 2nd APPROACH -> WRITING
# path = Path.cwd() / "temperatures.csv"
# file = path.open(mode="w", encoding="utf-8", newline="\n")
# writer = csv.writer(file)
# for temp_list in daily_temperatures:
#     writer.writerow(temp_list)

# file.close()

# *********************************************** 3rd APPROACH -> WRITING
# path = Path.cwd() / "temperatures.csv"
# with path.open(mode="w", encoding="utf-8", newline="\n") as file:
#     writer = csv.writer(file)
#     for temp_list in daily_temperatures:
#         writer.writerow(temp_list)

# *********************************************** 4th APPROACH -> WRITING
# path = Path.cwd() / "temperatures.csv"
# with path.open(mode="w", encoding="utf-8", newline="\n") as file:
#     writer = csv.writer(file)
#     writer.writerows(daily_temperatures)
