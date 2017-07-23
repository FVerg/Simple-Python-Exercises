# In this exercise we'll cover the usage of custom functions
# In the previous lectures, we've already used a lot of functions, but they
# were already defined by Python itself (print, dir, upper, etc.)

# In this exercise we're going to define our custom functions

# Let's assume we want to create a function which converts dollars to euros

# It will take 2 parameters:
# 1. Rate: The exchange rate from euros to dollars
# 2. Euros: The amount of euros to convert
# The parameters represent the input of the function

def currency_converter (rate, euros):
    dollars = float(euros)*rate
    return dollars

# Some things to notice:
# - The name of the function is the one following the keyword def: currency_converter
# - The code of the function is specified in the lines after the ":", and must be
#   written with at least one space from the beginning of the line. Otherwise
#   Python won't understand that the code belongs to the function we are defining.
# - The parameters (the ones inside the "()" brackets) specify an input for the function.
# - The return keyword allows the function to specify an output.
# - So, the function currency_converter has:
#     - INPUT: rate, euros
#     - OUTPUT: dollars
# - In consequence of what we just said, INDENTATION IS CRUCIAL in Python

# In order to use the function, we have to call it

input_euros = input ("Insert the amount of euros to convert:")

# In the following line we are calling the function currency_converter and
# we are passing it the parameters:
# rate = 1.8
# euros = input_euros (Inserted by the user)
output_dollars = currency_converter(1.18, input_euros)

print ("The corresponding amount in dollars is: ", output_dollars)

# Let's define and use some other functions:

def minutes_to_hours (minutes):
    return float(minutes)/60

inputMinutes = input ("Insert an amount in minutes:")
outputHours = minutes_to_hours (inputMinutes)
print ("The corresponding amount in hours is: ", outputHours)
