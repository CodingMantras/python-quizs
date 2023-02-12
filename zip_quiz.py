from itertools import zip_longest

numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c"]

print(list(zip(numbers, letters)))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Place 'None' where one list is exhausted
print(list(zip_longest(numbers, letters)))
# Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]
