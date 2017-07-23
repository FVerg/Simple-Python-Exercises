#Please create a function that converts Celsius degrees to Fahrenheit.

def celsius_to_fahrenheit (celsius):
    return float(celsius)*(9/5)+32

# Test the function

inputCelsius = input ("Insert a temperature in celsius: ")
outputFahrenheit = celsius_to_fahrenheit(inputCelsius)
print ("The corresponding temperature in Fahrenheit is: ", outputFahrenheit, " °F")
