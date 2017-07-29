# In this application we are going to build the first real world program.
# The program will take from the user three inputs:
# First letter: vowel or consonant
# Second letter: vowel or consonant
# Third letter: vowel or consonant
# And will emit 10 different words, according to the choices of the user.

# First of all we want to generate random letters
# To do this, we'll need the string module (built in)

import string

# This library has an object, called ascii_letters which contains the entire alphabet
# There is ascii_lowercase, which contains only lowercase letters.
# We need to pick a random letter from this string.

# There is the random module in Python

import random

# The specific method we are interested in is the choice method, which extracts
# a random element from a sequence of elements

# c = random.choice (string.ascii_lowercase)

# This line of code would return a random lowercase letter of the alphabet
# We want to limit the random pick to vowels and to consonant, separately

# So, we first define a function which generates a string of 3 letters
# without doing any consideration on its being a vowel or consonant.

def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3 # This will be our output string
    return name

name = generator()

print (name)

# The next step is to ask users what they want as a letter, if a vowel or consonant
# We'll do this in the second version of Word Generator
