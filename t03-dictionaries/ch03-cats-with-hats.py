# import time
import timeit


# Dictionary version
def cats_with_hats(cats):
    for mod_num in range(1, 101):
        for cat_num, has_hat in cats.items():
            if cat_num % mod_num == 0:
                cats[cat_num] = False if has_hat else True
    return cats


cats1 = {num : False for num in range(1, 101)}
# start_time = time.perf_counter()
dict_time = timeit.timeit(lambda: cats_with_hats(cats1), number=1)
# end_time = time.perf_counter()
# elapse_time = end_time - start_time
# print(f"\nFunction DICTIONARY execution time: {elapse_time:.6f} seconds")

# Printing the cats with hats
# cats_wit_hats = [key for key, value in cats.items() if value]
# print(cats_wit_hats)

print(f"\nFunction DICTIONARY execution time: {dict_time:.6f} seconds")


# List version
def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    # We want to walk around the circle 100 times
    for num in range(1, 100 + 1):
        # Each time we walk around, we visit 100 cats
        for cat in range(1, 100 + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                # Remove or add hat depending on
                # whether the cat already has one
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True

    # Add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)

    # Return the resulting list
    # return cats_with_hats_on


# Cats contains whether each cat already has a hat on,
# by default all are set to false since none have been visited
cats2 = [False] * (100 + 1)
# start_time = time.perf_counter()
lst_time = timeit.timeit(lambda: get_cats_with_hats(cats2), number=1)
# end_time = time.perf_counter()

# elapse_time = end_time - start_time
# print(f"\nFunction LIST execution time: {elapse_time:.6f} seconds")

# print(cats_wit_hats)

print(f"\nFunction LIST execution time: {lst_time:.6f} seconds")
