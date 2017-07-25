# In this lecture we are going to cover the reading of files.
# Python can be used to read both textual and binary files.

# In this code snippet we're going to read the content of a file.
# For this purpose we'll use the file "15_Text_File.txt"

# To read the content of a file we must open the file first:

file = open ("15_Text_File.txt", 'r')

# The open method takes two parameters:
# 1. The name of the file to open
# 2. The type of operations to do on the file
#    - 'r': read
#    - 'w': write


# The type of the file will be a TextIOWrapper which is an internal Python
# representation of a file.
# ATTENTION: Python uses files as same as the other programs, so, if we try
# to delete a file which is opened in a Python program we'll get an OS error.

print (type (file))

# To get the content of the file, we use the read() method

content = file.read()

# Printing the variable, the content of the file will be printed

print (content)

# Differently from the file variable, the one we used to store the content
# of the file will be of type str

print (type (content))

# In some cases it would be useful to store the content of a file in a list.
# This can be done with the method readlines()

lst = file.readlines()

print (lst)

# As you may notice from the output of the program, the list is empty.
# That's because python holds an internal pointer which points to the line of
# the file to read. Having used the read() method first, the pointer will now
# point at the end of the file. So, when we're using readlines(), we start reading
# the file from the last line, so we'll insert nothing into the list.

# To solve this problem and make the internal pointer to point to the beginning
# of the file again, we can use the seek() method, passing it 0 as argument, which
# refers to the beginning of the file.

file.seek(0)

lst = file.readlines()

print (lst)

# Each line ends with "\n", which means "NEXT LINE"

# To cleanup our list, and remove the /n from each element we can do:

lst = [i.rstrip("\n") for i in lst]

# This line of code, for each element of the list, will apply the rstrip method
# which removes the substring passed as parameter from the considered string,
# in this case "\n".

print (lst)

# We need now to close the file.

file.close()

# This is a crucial operation: if we open a file in write mode, and close the
# terminal without closing the file, the modifications we applied on the file
# won't be saved.

# Once the content of a file is read and stored into a variable, the file can
# be deleted without problems. The variables won't be affected.
