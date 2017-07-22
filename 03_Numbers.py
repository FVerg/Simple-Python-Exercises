# Using variables to store numbers and print a sum of two variables

print ("a = 2; b = 3; a + b = ")
a = 2
b = 3

print (a+b)

# Function type: returns the type of a variable

print ("a is of type: ")
print (type(a))

inputNumber = input ("Insert a number (integer or float): ")
print ("The inserted number is of type: ", type(inputNumber))

# As you'll see on the console, the inserted number will always be treated as a string
# So if we want to add a certain number to the one inserted from keyboard (inputNumber)
# the latter has to be converted to an integer

print ("The inserted number + 10 is equal to: ")

# int (nameVariable): converts the variable nameVariable to integer
outputNumber = int(inputNumber) + 10;

print (outputNumber)

# On the other hand, adding a float and an integer will not cause any errors
# because Python will automatically consider both numbers as floats

intNumber = 10
floatNumber = 1.2

print ("intNumber is of type: ", type(intNumber))
print ("floatNumber is of type: ", type (floatNumber))

outputSum = intNumber+floatNumber

print (outputSum)
print ("The sum of the intNumber and floatNumber is of type: ", type (outputSum))
