# In this lecture we'll cover the usage of the with statement.

# The with statement allows to close a file without using the close method.
# The with statement defines a block, which will close the file once left.

# In the block defined the variable file can be used
with open("18_Text_File.txt", 'a') as file:
    file.write ("Line 4 \n")

# The file will be closed automatically.
