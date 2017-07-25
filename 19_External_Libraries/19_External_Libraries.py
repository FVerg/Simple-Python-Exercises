# In this lecture we're going to cover the usage of external libraries and modules.

# Modules and external libraries allow the user to load and use inside his program
# different type of function which are not loaded into the Python program by default,
# as it happens for the most used functions like print, open etc.

# We now import the "os" library:

import os

# One of the functionalities offered by os is the one to put inside a list
# all the file names in the current directory. This may be very useful for
# some purposes, like merging files.

files = os.listdir()

# files will contain the list of files in this directory

print (files)

# There are also other libraries, called PACKAGES that do not come with
# the Python installation.

# To download and install a package you just need to run the terminal (cmd.exe)
# and type: pip install "PackageName"

# After that, the package can be imported as well as libraries and modules, through
# import method.

# We now install through cmd.exe the glob2 library, for example

import glob2

# glob(*) returns all the files in the directory
# glob(*.txt) returns all the txt files in the directory
print (glob2.glob("*.txt"))
