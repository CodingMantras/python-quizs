import itertools

input = [3, 4, 6, 5, 7, 6, 2, 4, 9, 8, 2]

fill_15 = [[i, j, k]
           for i in input for j in input for k in input if (i + j + k) == 15]

# Repetitive
print(fill_15)
print(len(fill_15))     # Output: 130

# Unique
fill_15.sort()
unique_15 = [fill_15 for fill_15, _ in itertools.groupby(fill_15)]
print(unique_15)
print(len(unique_15))   # Output: 46
