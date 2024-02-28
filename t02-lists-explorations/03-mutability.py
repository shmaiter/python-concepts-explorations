"""
Mutable Objects: lists, sets and dictionaries.
Depending on the object's depth levels you mith consider using
a "shallow copy" or a "deep copy".
"""

# ***************************************************** Example 1  *****************************************************
# outer_lst = [1, 2, 3, 4, 5, 6]
# def test_func(lst):
#     # The outer list will be modify as well
#     lst[0] = "X"
#     print(f"Inside function: {lst}")  # ["X", 2, 3, 4, 5]


# test_func(outer_lst)
# print(f"Outside function {outer_lst}")  # ["X", 2, 3, 4, 5]


# ***************************************************** Example 2  *****************************************************
# outer_lst = [1, 2, 3, 4, 5, 6]
# def test_func(lst):
#     # Only the inner recently copied list will be modify
#     copy_lst = lst[:]  # Shallow copy, one level deep copy. The children remain as references to the original
#     copy_lst[0] = "X"
#     print(f"Inside function: {copy_lst}")  # ["X", 2, 3, 4, 5]


# test_func(outer_lst)
# print(f"Outside function {outer_lst}")  # [1, 2, 3, 4, 5]


# ***************************************************** Example 3  *****************************************************
# outer_lst = [[1, 2], [3, 4], [5, 6]]


# def test_func(lst):
#     # Another way to make one level deep copy is with the constructor
#     copy_lst = list(lst)
#     # When we modify the children on the first sublist, the outer list changes as well
#     copy_lst[0][0] = "X"
#     print(f"Inside function: {copy_lst}")  # [["X", 2], [3, 4], [5, 6]]


# test_func(outer_lst)
# print(f"Outside function {outer_lst}")  # [["X", 2], [3, 4], [5, 6]]

# ***************************************************** Example 4  *****************************************************
import copy

outer_lst = [[1, 2], [3, 4], [5, 6]]


def test_func(lst):
    copy_lst = copy.deepcopy(lst)
    copy_lst[0][0] = "X"
    print(f"Inside function: {copy_lst}")  # [["X", 2], [3, 4], [5, 6]]


test_func(outer_lst)
print(f"Outside function {outer_lst}")  # [[1, 2], [3, 4], [5, 6]]
