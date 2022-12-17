expression = "a" in "b", "a"

print(expression)


# Ans:
'''✨ The comma is not an operator in Python, but a separator   
between expressions. Therefore: ✨
'''
expression = "a" in "b", "a"

# ✅ Can be correctly written as:
expression = ("a" in "b"), "a"

# ❌ But not like this:
expression = "a" in ("b", "a")
