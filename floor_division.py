'''✨ Python Quiz: What would be the output 
of the code below??? ✨
'''

expression = -32 // 10
print(expression)

# ⚡Output: ???

#############################################################
# Ans:

'''It's primarily driven by the integer division has to return the floor. 
C also requires that identity to hold, and then compilers that truncate 
i // j need to make i % j have the same sign as i.

There are few real use cases for i % j when j is negative. 
When j is positive, there are many, and in virtually all of them 
it's more useful for i % j to be >= 0. 

If the clock says 10 now, what did it say 200 hours ago? 
-190 % 12 == 2 is useful; -190 % 12 == -10 is a bug waiting to bite.
'''
