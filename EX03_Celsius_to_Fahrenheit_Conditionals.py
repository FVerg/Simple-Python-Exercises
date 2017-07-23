# In exercise 1 you created a function that converted Celsius degrees to Fahrenheit.

# The lowest possible temperature that physical matter can reach is -273.15 °C.
# With that in mind, please improve the function by making it print out a message
# in case a number lower than -273.15 is passed as input when calling the function.


def celsius_to_fahrenheit (celsius):
    return float(celsius)*(9/5)+32

inputCelsius = input ("Insert a temperature in celsius: ")

if float(inputCelsius) < -273.15:
    print ("It is not physically possible to have such a low temperature")
else:
    print ("The corresponding Fahrenheit temperature is: ", celsius_to_fahrenheit(inputCelsius), " °F")
