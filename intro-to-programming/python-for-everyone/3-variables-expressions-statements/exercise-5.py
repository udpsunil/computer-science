# Write a program which prompts the user for a Celsius temperature
# convert the temperature to Fahrenheit and print out the converted
# temperature.

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9.0 / 5.0 + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")
