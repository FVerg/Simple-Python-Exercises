# Exercise #5: File Handling

# Here's a rather challenging exercise that integrates functions, loops, conditionals, and file handling.

# In exercise 4, you recursively printed out converted temperature in the command line.
# For this exercise, please consider the same list of Celsius values again as input:

temperatures=[10,-20,-289,100]

# Try to make a script that converts Celsius to Fahrenheit and creates a text file
# and stores the converted values inside the text file. Your text file content should
# look like this:

# 50.0
# -4.0
# 212.0

# Please don't write any message in the text file when input is lower than -273.15.


def celsius_to_fahrenheit (celsius):
    return float(celsius)*(9/5)+32

with open ("EX05_Text_File.txt", "w") as file:
    for temp in temperatures:
        if temp >= -273.15:
            ftemp = celsius_to_fahrenheit(temp)
            file.write (str(ftemp) + "\n")
