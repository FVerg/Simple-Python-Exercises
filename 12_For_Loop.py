# In this lecture we'll cover the fundamentals of loops.
# A loop is basically a way to execute a statement multiple times.
# Loops allow to save a lot of code, and avoid some replications.
# In Python there are two different loops: for and while

emails = ["foo@email.com", "me@gmail.com", "you@hotmail.com"]

# If we want to print each item inside the list, we can do by using one print
# function for each item of the list, but this implies some kind of replication of code.
# The for loop is very useful in a case like this:

for email in emails:
    print (email)

# The previous two lines print the item of the list, for each item

# Suppose that we want to print only the gmail addresses:

for email in emails:
    if email.endswith("@gmail.com"):
        print (email)

# We can do the same using the operator in:

for email in emails:
    if "gmail" in email:
        print (email)
