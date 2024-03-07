from pathlib import Path
import csv
from matplotlib import pyplot as plt

# 1. Read in the file pirates.csv from the Chapter 17 practice files folder.
filepath = Path.cwd() / "pirates.csv"
with filepath.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    years = []
    temperatures = []
    pirates = []
    for item in reader:
        years.append(int(item["Year"]))
        temperatures.append(float(item["Temperature"]))
        pirates.append(int(item["Pirates"]))

# 2. Create a line graph of the average world temperature in degrees
# Celsius as a function of the number of pirates in the world—
# that is, graph Pirates along the x-axis and Temperature along
# the y-axis
plt.plot(temperatures, pirates, "g-o")


# Label data points with year
for i, year in enumerate(years):
    plt.annotate(
        year,
        (temperatures[i], pirates[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )


# 3 Add a graph title and label your graph’s axes
plt.title("Relation btw Pirates on Changes on Temperature")
plt.xlabel("Temperatures")
plt.ylabel("Amount of Pirates")

# 4. Save the figure
plt.savefig("pirates_temp.png")

# Show the plot
plt.grid(True)
plt.show()
