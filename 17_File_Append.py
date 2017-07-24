# In this lecture we are going to cover the append file.

# As we briefly said in the previous lecture, we can write new strings into
# a file appending the new content without overwriting the previous one.

# For this to be done, we need to open a file in append mode 'a'

file = open ("17_Text_File.txt", 'a')

file.write ("Line 1 \n")
file.write ("Line 2 \n")

file.close()


# Obviously, in this way each time we execute the program we'll append the content
# to the file, without deleting the previous contents.
