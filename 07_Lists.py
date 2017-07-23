# In this lecture we are going to cover the usage of lists.
# As we'll see, lists are very similar to strings, in the way we looked at them
# in the previous exercise (06_Indexing.py). That's because they both represent
# a sequence of items. A string is a sequence of strings. A list is a sequence
# of any type. A list can contain different data types simultaneously!

mylist = ["H", 2, 1.1]

# Lists share the same indexing system as strings, as we saw on the previous ex.
print ("Element of index ", 0, " contains: ", mylist[0])
print ("Element of index ", 1, " contains: ", mylist[1])
print ("Element of index ", 2, " contains: ", mylist[2])

print ("Element of index ", 0, " is of type: ", type(mylist[0]))
print ("Element of index ", 1, " is of type: ", type(mylist[1]))
print ("Element of index ", 2, " is of type: ", type(mylist[2]))

# As well as strings, lists have methods available on them:

print ("Methods available on mylist: ", dir(mylist))

# append(item): Adds the item specified at the end of the list

print ("Before the append: ", mylist)
mylist.append("Hello")
print ("After the append: ", mylist)

# remove (item); Removes the item specified

print ("Before the remove: ", mylist)
mylist.remove("Hello")
print ("After the remove: ", mylist)
