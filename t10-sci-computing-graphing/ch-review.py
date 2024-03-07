import numpy as np

# 1. Create a 3 × 3 NumPy array named first_matrix that includes the
# numbers 3 through 11 by using np.arange() and np.reshape().
matrix1 = np.arange(3, 12).reshape(3, 3)
print("\n", matrix1)

# 2. Display the minimum, maximum and mean of all entries in first_-
# matrix.
min = matrix1.min()
max = matrix1.max()
mean = matrix1.mean()
print("\n", min, max, mean)

# 3. Square every entry in first_matrix using the ** operator, and save
# the results in an array named second_matrix.
matrix2 = matrix1 * matrix1
print("\n", matrix2)

# 4. Use np.vstack() to stack first_matrix on top of second_matrix and
# save the results in an array named third_matrix.
matrix3 = np.vstack([matrix1, matrix2])
print("\n", matrix3)

# 5. Use the @ operator to calculate the matrix product of third_matrix
# by first_matrix.
matrix4 = matrix3 @ matrix1
print("\n", matrix4)

# 6. Reshape third_matrix into an array of dimensions 3 × 3 × 2.
matrix3_reshaped = matrix3.reshape(3, 3, 2)
print(matrix3_reshaped)