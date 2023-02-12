'''🚀 Fun with String comparison in Python
'''
# 💎 Guess the output of this code
print("8" > "11")       # 👩‍💻Output: True
print("Two" > "Three")  # 👩‍💻Output: True
print("Four" < "One")   # 👩‍💻Output: True
print("hello" == "HELLO")   # 👩‍💻Output: False
print("😀" > "😉")      # 👩‍💻Output: False

################################################
# 💎 Can you guess the reason behind this unusual behavior
# 💎 You need to understand the UNICODE value of each character

print(ord('8'))     # 👩‍💻Output: 56
print(ord('1'))     # 👩‍💻Output: 49
print(ord('w'))     # 👩‍💻Output: 119
print(ord('h'))     # 👩‍💻Output: 104

# Python compare two strings in the order of their unicode values.
# You can check the unicode values of other characters to get the
# answers of all the print statements given above.
#####################################################
# 🎯 @CodingMantras
# See you soon, till then Keep Improving 🤝!!!
