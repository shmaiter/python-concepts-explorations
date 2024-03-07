from matplotlib import pyplot as plt
import numpy as np

# xs = [1, 2, 3, 4, 5]
# ys = [2, 4, 6, 8, 10]

# plt.plot(xs, ys)
# plt.show()

# negative values
# xs = [1, 2, 3, 4, 5]
# ys = [3, -1, 4, 0, 6]
# plt.plot(xs, ys)
# plt.show()

# green dots over line
# plt.plot([2, 4, 6, 8, 10], "g-o")
# plt.show()

# Plot Multiple Graphs in the Same Window
# xs = [0, 1, 2, 3, 4]
# y1 = [1, 2, 3, 4, 5]
# y2 = [1, 2, 4, 8, 16]
# # plt.plot(xs, y1, xs, y2)
# # If you want to control the style of each graph
# plt.plot(xs, y1, "g-o", xs, y2, "b-^")
# plt.show()

# 2 dimensional arrays
data = np.arange(1, 21).reshape(5, 4)
print(data)
# data now contains the following array:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]

# plt.plot(data)  # each column is a line
plt.plot(data.transpose())  # each row is a line
plt.show()
