def convert_fahrenheit_to_celcius():
    fahrenheit = int(input("Enter a temperature in fahrenheit: "))
    celcius = (fahrenheit - 32) * 5.0/9.0
    print(fahrenheit, "Fahrenheit = ", celcius, "˚C")

def convert_celcius_to_fahrenheit():
    celcius = int(input("Enter a temperature in celcius: "))
    fahrenheit = 9.0/5.0 * celcius + 32
    print(celcius, "˚C = ", fahrenheit, "Fahrenheit")



user = input("Do you want to convert from Celcius (Enter C) or Fahrenheit(Enter F)?: ").upper()

if user == "C": convert_celcius_to_fahrenheit()
if user == "F": convert_fahrenheit_to_celcius()
