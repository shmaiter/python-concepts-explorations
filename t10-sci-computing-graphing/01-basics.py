import numpy as np

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # ic(matrix * 2)
# # ic(matrix * matrix)

# # Get a tuple of axis length
# matrix.shape  # (3, 3)
# # Get an array of the diagonal entries
# matrix.diagonal()  # array([1, 5, 9])
# # Get a 1-dimensional array of all entries
# matrix.flatten()  # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# # Get the transpose of an array
# matrix.transpose()  # array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
# # Calculate the minimum entry
# matrix.min()  # 1
# # Calculate the maximum entry
# matrix.max()  # 9
# # Calculate the average value of all entries
# matrix.mean()  # 5.0
# # Calculate the sum of all entries
# matrix.sum()  # 45

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# np.vstack([A, B])
# np.hstack([A, B])

# matrix = np.arange(1, 10)  # ([1, 2, 3, 4, 5, 6, 7, 8, 9])
# matrix = matrix.reshape(3, 3)
# print(matrix)
# # array([ [1, 2, 3],
# #         [4, 5, 6],
# #         [7, 8, 9]])

print(np.arange(1, 13).reshape(3, 2, 2))
# [[[ 1  2]
#   [ 3  4]]

#  [[ 5  6]
#   [ 7  8]]

#  [[ 9 10]
#   [11 12]]]

# Matrices of random data
np.random.random([3, 3])
# array(
#     [
#         [0.27721176, 0.66206403, 0.20722988],
#         [0.15722803, 0.06286636, 0.47220672],
#         [0.55657541, 0.27040345, 0.24558674],
#     ]
# )
