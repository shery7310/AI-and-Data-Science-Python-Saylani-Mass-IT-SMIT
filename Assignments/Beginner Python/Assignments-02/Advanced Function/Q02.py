"""
Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.
Fahrenheit = Celsius × 1.8 + 32 according to www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html
Celsius = (Fahrenheit - 32) / 1.8
0 °F = -17.77778 °C
0 °C = 32 °F
"""
temperature = float(input("Enter Temperature:\n"))

def convert_celsius(temp: float):
    """
    If temperature is entered here it means it's currently in fahrenheit and we need to convert it to celsius
    """
    if temp == 0:
        return -17.77778 # 0 °F = -17.77778 °C
    else:
        celsius = (temp - 32) / 1.8
        return celsius

def convert_fahrenheit(temp: float):
    """
    If temperature is entered here it means it's currently in celsius and we need to convert it to fahrenheit
    """
    if temp == 0:
        return 32 # 0 °C = 32 °F
    else:
        fahrenheit = temp * 1.8 + 32
        return fahrenheit

choice = input("Enter c for convert temperature to celsius and f to convert temperature to Fahrenheit:\n").lower()
if choice == 'c':
    print(f"The temperature in Celsius is {convert_celsius(temperature)}°C")
elif choice == 'f':
    print(f"The temperature in Celsius is {convert_fahrenheit(temperature)}°F")
else:
    print("Invalid Choice Try Again")
