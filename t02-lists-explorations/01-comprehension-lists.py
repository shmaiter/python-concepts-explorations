import random

brands = ['honda', 'yamaha', 'suzuki', 'fullbeck', 'quixia']


# matrix_1 = [brand for brand in brands for number in range(5)]
# matrix_1 = []
# for brand in brands:
#     for number in range(5):
#         matrix_1.append(brand)

# print(matrix_1)


# matrix_2 = [[j for j in range(5)] for i in range(5)]
# matrix_2 = []
# for i in range(5):
#     matrix_2.append([])
#     for j in range(5):
#         matrix_2[i].append(j)

# print(matrix_2)


matrix_3 = [[random.randint(0,1) for i in range(5)] for j in range(5)]
# matrix_3 = []
# for i in range(5):
#     matrix_3.append([])
#     for j in range(5):
#         matrix_3[i].append(random.randint(0,1))

print(matrix_3)


