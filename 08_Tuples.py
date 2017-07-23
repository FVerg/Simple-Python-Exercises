# In this lecture we'll cover the usage of tuples.
# Tuples in Python are very similar to lists, but unlike them,
# TUPLES ARE IMMUTABLE: you can't change its content once defined.

# Tuples will be used in very specific cases. Lists are much more widespread

t = ("Hello", 1, 2.2, "h")

print (t);

print ("Methods available on tuples: ", dir (tuple))

# As you'll notice, the methods available for tuples are slightly different
# in number from the ones available for lists. That's because, as we've already
# said, they are NOT MUTABLE, so you can't add or remove elements as we did
# in the previous exercise

# count(item): Returns the number of occurrencies of the specified item inside a tuple:

print ("Hello is present ", t.count("Hello"), " times in the tuple")
