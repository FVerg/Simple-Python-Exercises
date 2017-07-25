# In this lecture we are going to cover the while loop.
# It allows to execute a piece of code for a certain number of times.
# More in detail, the code inside a while loop gets executed as long as the
# condition specified in the head of the while is true.

# Let's suppose we want to create a program which waits for a password
# and keeps asking for it until the right one is entered.

inputPassword = ""

while inputPassword != "python123":
    inputPassword = input ("Insert password: ")
    if (inputPassword == "python123"):
        print("Login successful")
    else:
        print("Wrong password, try again")
