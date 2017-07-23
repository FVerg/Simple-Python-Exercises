# In this exercise, we'll cover the usage of math operators
# First of all, let's see how some different operators used together work

result = 20-10/5*3**2

print (result)

# Python will execute the operations in this order:
# 1. Exponential (**): 2**3 equals to 2^3 = 2*2*2 = 8
# 2. Division and multiplication (On the same level: what comes first from left to right is executed first)
# 3. Addition and subtractions (On the same level: what comes first from left to right is executed first)

# So, this line of code will do:
# 3**2 = 9
# 10/5 = 2
# 20 - (2*9) = 20-18 = 2.0

# The result will be 2.0 (a float) and not just 2 (an int) because of the presence
# of the division (10/5). In Python 3 the division always outputs a float

# Obviously the result changes if we use the brackets:

result = (20-10)/5*3**2

print (result)

# This way, the operations in the brackets gets executed first, so, in order:
# 20 - 10 = 10
# 10 / 5 = 2.0
# 3**2 = 9
# 2.0 * 9 = 18.0
