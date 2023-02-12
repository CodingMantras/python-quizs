'''Python doc says: 
-------------------------------------------
operator.__iadd__(a, b)
a = iadd(a, b) is equivalent to a += b.

Operator += calls __iadd__ method first at the backend,
which is an (in-place addition). 
If the object does not support the __iadd__ method, 
Python will fall back to the __add__.

Which is the case when we use extend on a list.
It means it is equal to calling the extend method.

But append calls __add__ method.
-------------------------------------------
'''

# A: ["Python", "Java"]
# B: ['Python', 'J', 'a', 'v', 'a']
# C: Error

lang_1 = ["Python"]
lang_2 = ["C", "Ruby"]
# lang_1 += lang_2
lang_1.append(lang_2)
lang_1 += "Java"
# lang_1.extend("Java")
print(lang_1)
