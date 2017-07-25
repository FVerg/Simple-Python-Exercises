# In this lecture we'll cover the usage of conditionals.
# A conditional is composed by different blocks of code which will be executed
# or not basing on the value of a given conditional (True or false)

inputValue = input("Insert a number: ")


if int(inputValue) < 10:
    print ("The inserted number is less than 10")
else:
    print ("The inserted number is greater or equal to 10")

# The previous code will print something if the condition specified in the if clause
# is true, and another thing if it is false.

# It is possible to define different behaviors of the code by using the elif clause
# It will be validated only if the first if clause is not True

if int(inputValue) == 10:
    print ("The inserted number is 10")
elif int (inputValue) == 9:
    print ("The inserted number is 9")
else:
    print ("The inserted number isn't 9 nor 10")


# It is possible to use conditional in conjunction of function definition

def insert_age():
    age = input("Insert your age: ")
    if int(age) > 110:
        print ("It is not possible you have that age, unless you are immortal!")
    else:
        print ("Your age is: ", age)


insert_age()
