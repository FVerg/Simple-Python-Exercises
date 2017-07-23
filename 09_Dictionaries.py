# In this lecture we'll cover the usage of dictionaries.
# A dictionary is like a list with custom indexes.
# In lists, Python automatically assigns indexes to the contained items
# In dictionaries, the indexes are specified by the programmer, and can be
# different from numbers.

# List:
l = [1, 2, 3]

# Dictionary:
d = {"Name":"John", "Surname":"Smith"}

# Name and Surname: Indexes
# John and Smith: Values

# So we can access to the items of the dictionaries by indexing them using the
# specified index:

print (d["Name"])
print (d["Surname"])

# Dictionaries are UNORDERED collections of items

# Dictionaries can contain also complex types, like lists and tuples:

d = {"Names":["John", "Mark", "Tim"], "Surnames":["Smith", "Baker", "Roth"]}

print (d["Names"])
print (d["Surnames"])

# You can also index the lists inside the dictionaries

print (d["Names"][0])
print (d["Names"][1])
print (d["Names"][2])

print (d["Surnames"][0])
print (d["Surnames"][1])
print (d["Surnames"][2])
