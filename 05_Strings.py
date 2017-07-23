# In this exercise we'll cover the usage of strings.
# A string is everything that goes inside quotes "..."

inputString = input ("Insert a string: ")

print ("The inserted string is: ", inputString)

# Strings in python are very powerful. Let's assume we want to replace, if present
# the letter a with the letter b, inside a string
# ball -> bbll

editedString = inputString.replace("a", "b")

print ("The edited string, with a replaced with b is: ", editedString)

# replace ("oldLetter", "newLetter"): will replace each occurrence of oldLetter
# with newLetter. You can also specify how many occurrences to replace
# by inserting a third parameter: replace ("old", "new", #occurrences)

editedString2 = inputString.replace ("a", "b", 1)
print ("The edited string, with the first 'a' replaced with 'b' is: ", editedString2)

# If you want to print all the available methods for a certain variable
# you can use the method: dir(variable)

print ("On the string inputString you can use: ")
print (dir(inputString))

# upper(): transforms the string on which is called on to upper case

print ("The string you inserted before transformed uppercase: ")
print (inputString.upper())

# String supports operators to. They implement concatenation:

print ("Concatenation: ")
print (editedString + editedString2)
