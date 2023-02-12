# 📋 Do consider the chaining operation of Python here.
# Just like this: 💥 3 > x > 10 💥
####################################################

# 👩‍💻 Let's see some examples here, first.
print(False == False)   # Output: True

print((False == False) in [False])  # Output: False
# 👉 As this will evaluate to: True in [False]
#####################################################

# 📜 But the question here is
print(False == False in [False])

# 🔥 In other way, after considering the chaining operation,
# It can be evaluated to:
print(False == False and False in [False])
# further: print(True and True)
# 🚀 So the answer is: True

#####################################################
# 🎯 @CodingMantras
# See you soon, till then Keep Improving 🤝!!!
