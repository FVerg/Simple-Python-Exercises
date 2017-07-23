# Exercise 04: given a list of temperatures, apply the converting function
# created in EX03 for each one of them

temperatures = [10, -20, -289, 100]

def celsius_to_fahrenheit (celsius):
    return float(celsius)*(9/5)+32

for temperature in temperatures:
    fahrenheit = celsius_to_fahrenheit(temperature)
    if fahrenheit < -273.15:
        print ("It is not physically possible to have such a temperature")
    else:
        print ("The corresponding Fahrenheit temperature is: ", fahrenheit, " °F")
