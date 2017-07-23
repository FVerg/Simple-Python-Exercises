# In this lecture we are going to cover the indexing. That is a very useful
# characteristic of Python data types. Let's talk about string indexing.

c = "Hi everyone!"

# For each item composing the string, Python holds under the hood a number
# he uses to identify and access each item, in this case, each char.
# In this case we'll have:
# [0]: H
# [1]: i
# [2]:
# [3]: e
# ...


print ("Character at index ", 0, ": ", c[0])
print ("Character at index ", 1, ": ", c[1])
print ("Character at index ", 2, ": ", c[2])
print ("Character at index ", 3, ": ", c[3])
print ("Character at index ", 4, ": ", c[4])
print ("Character at index ", 5, ": ", c[5])

# And so on...

# If we look at the type of the extracted characters, we'll se that it is a
# type string. So we can say that a string is made of strings.

print ("Character at index ", 0, " is of type: ", type (c[0]))


# Pyhon also allows to do an inverted indexing, counting items from the end
# of the collection (in this case a string).

print ("Character at index ", -1, ": ", c[-1])
print ("Character at index ", -2, ": ", c[-2])
print ("Character at index ", -3, ": ", c[-3])
print ("Character at index ", -4, ": ", c[-4])
print ("Character at index ", -5, ": ", c[-5])
print ("Character at index ", -6, ": ", c[-6])

# And so on...

# It is possible to extract more than one part of the string simultaneously.
# If we want to extract the word i (indexes 0 to 1) we can do:

print ("Characters at index from [0] to [1]: ", c[0:2])

# Look that we indexed the string with [0:2]. That's because Python indexes
# collections in an UPPER BOUND EXCLUSIVE way: the indicated upper bound will
# not be included in the output. So, indexing [0:2] will extract items [0] and [1]
# but not item [2]

#There are also some shortcuts, like this one:

print ("Characters at index from [0] to [1]: ", c[:2])

# Prints the same exact thing of the previous line.

# Another shortcut:

print ("Characters at index from [3] to end: ", c[3:])
