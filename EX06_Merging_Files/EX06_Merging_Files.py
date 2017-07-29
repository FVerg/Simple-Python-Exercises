# EX06: Merging files
# Create a script that merges the three text files into a new text file containing
# the text of all three files. The filename of the merged text file should contain
# the current timestamp down to the millisecond level. E.g. "2016-06-01-13-57-39-170965.txt".

import datetime

filename = datetime.datetime.now()

filename = filename.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

content1 = ""
content2 = ""
content3 = ""

with open ("file1.txt", "r") as file:
    content1 = file.read()

with open ("file2.txt", "r") as file:
    content2 = file.read()

with open ("file3.txt", "r") as file:
    content3 = file.read()

with open (filename, "a") as file:
    file.write (content1 + "\n")
    file.write (content2 + "\n")
    file.write (content3 + "\n")
