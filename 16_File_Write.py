# In this lecture we are going to cover the writing of files.
# We are going to write something inside a file.

# Open the file in write mode

file = open("16_Text_File.txt", 'w')

# If the file name specified does not refer to an existing file, a file with That
# name will be created

# Write a string into the file:

file.write ("Line 1 \n")
file.write ("Line 2 \n")

# Every time we use the write function on a file opened in 'w' mode, we are going
# to overwrite the previous content of the file. We can, in 'w' mode, write more
# than one string inside the file obviously, but if we execute again the program,
# at the first call of file.write the content will be overwritten.
# In order to write something new and append the new content to the existing one
# we need to open the file in APPEND MODE (We'll cover append mode in the next lecture)

lst = ["Line 3", "Line 4", "Line 5"]

for l in lst:
    file.write (l+"\n")
file.close()
