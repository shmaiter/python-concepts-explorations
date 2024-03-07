from matplotlib import pyplot as plt
import numpy as np

days = np.arange(0, 21)
other_site = np.arange(0, 21)
real_python = other_site ** 2
# print(other_site)
# print(real_python)

plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks(range(0, 21, 5))  # what numbers are gonna be shown on the x-axis
plt.xlabel("Days of Reading")
plt.ylabel("Amount of Python learned")
plt.title("Python Learned Reading Real Python vs. Other Site")
plt.legend(["Other Site", "Real Python"])  # Add them in the same order as the plots above
plt.show()
