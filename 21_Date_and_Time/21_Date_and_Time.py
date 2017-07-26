# In this lecture we are going to cover the usage of date and time in Python.

# The module including functions regarding date and time is datetime
import datetime

# To get the current date and time:

print (datetime.datetime.now())

# It will be a special data type: datetime. Not a string
print (type(datetime.datetime.now()))

# The returned date and time depend on the one set on your computer

# We can store an arbitrary date/time in a variable

yesterday = datetime.datetime(2017,7,25,18,55,0,0)
print ("Yesterday: " ,yesterday)

now = datetime.datetime.now()
print ("Now: ", now)

print ("Time passed: ", now-yesterday)

# The subtraction between two datatimes returns a delta time

print (type (now-yesterday))

# We can save it in a variable

delta = now - yesterday

# And access to its internal fields, such as days

print ("Passed days: ", delta.days)

# We can use datetime to create a file with that name
# We have to remove the column from the name of the file, because Windows
# does not allow to use columns as file names

filename = datetime.datetime.now()

# To format the date and time in a proper way, usable as a file name, we can do:

filename = filename.strftime("%Y-%m-%d-%H-%M-%S-%f")

# This way, we are going to extract from the string:
# %Y: The entire year (2017 not 17)
# %m: The month
# %d: The day
# %H: The hours
# %M: The minutes
# %S: The seconds
# %f: The milliseconds

# For more keywords, visit strftime.org

# The data type returned is a string
print (type (filename))

with open(filename, "a") as file:
    file.write("")

# With datetime objects is possible to calculate subsequent dates by adding
# a timedelta to a datetime

after = now + datetime.timedelta(days = 2)

print (now)
print (after)

after = now + datetime.timedelta (seconds = 200)

print (now)
print (after)

# There is also another module, time, that allow to put in our program some
# temporal information, like waiting.

import time

lst = []

for i in range (5):
    lst.append(datetime.datetime.now())
    time.sleep(1)                           # Sleep for 1 second

for i in lst:
    print (i)
