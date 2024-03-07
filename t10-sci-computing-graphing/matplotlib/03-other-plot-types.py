from matplotlib import pyplot as plt
from numpy import random

# Example #1
# xs = [1, 2, 3, 4, 5]
# tops = [2, 4, 6, 8, 10]
# plt.bar(xs, tops)
# plt.show()


# Example #2
# fruits = {
#     "apples": 10,
#     "oranges": 16,
#     "bananas": 9,
#     "pears": 4,
# }
# plt.bar(list(fruits.keys()), list(fruits.values()))
# plt.show()

# Example #3: Histogram
plt.hist(random.randn(10000), 20)
plt.savefig("histogram.png")  # save your graphs as images
plt.show()
