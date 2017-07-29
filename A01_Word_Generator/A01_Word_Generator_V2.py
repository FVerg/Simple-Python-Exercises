# In this application we are going to build the first real world program.
# The program will take from the user three inputs:
# First letter: vowel or consonant
# Second letter: vowel or consonant
# Third letter: vowel or consonant
# And will emit 10 different words, according to the choices of the user.

# We want to make the previous program more sophisticated in order to allow the
# user to decide for each letter if it has to be a consonant or a vowel.

import random, string


# First, we create two different strings, one containing vowels, one containing consonants
vowels = ""
consonants = ""
for i in string.ascii_lowercase:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
        vowels = vowels + i
    else:
        consonants = consonants + i

# Then we let the user choose the letters he wants in the name to be returned

choice1 = input ("First letter: you want it to be a vowel ('v') or a consonant ('c') or any ('l')? ")
choice2 = input ("Second letter: you want it to be a vowel ('v') or a consonant ('c') or any ('l')? ")
choice3 = input ("Third letter: you want it to be a vowel ('v') or a consonant ('c') or any ('l')? ")

namelist = []


def generator():
    name = ""

    if (choice1=='v'):
        name = name + random.choice(vowels)
    elif (choice1 == 'c'):
        name = name + random.choice (consonants)
    elif (choice1 == 'l'):
        name = name + random.choice (string.ascii_lowercase)
    else:
        name = name + choice1

    if (choice2=='v'):
        name = name + random.choice(vowels)
    elif (choice2 == 'c'):
        name = name + random.choice (consonants)
    elif (choice2 == 'l'):
        name = name + random.choice (string.ascii_lowercase)
    else:
        name = name + choice2

    if (choice3=='v'):
        name = name + random.choice(vowels)
    elif (choice3 == 'c'):
        name = name + random.choice (consonants)
    elif (choice3 == 'l'):
        name = name + random.choice (string.ascii_lowercase)
    else:
        name = name + choice3

    namelist.append(name)


for i in range (10):
    generator()

print (namelist)
