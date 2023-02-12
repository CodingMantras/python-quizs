from email.policy import strict


x = [1, 2, 3, 4, 5]  # len 5
y = ['a', 'b', 'c']  # len 3


#Syntax: zip(*iterable)
# stop iterating at 3
print(list(zip(x, y), strict=True))
