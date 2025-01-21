# Create a function that takes two numbers and returns their sum.

def add(num1, num2):
    num1, num2 = float(num1), float(num2)
    return num1 + num2

number1 = input("Enter Num1:\n")
number2 = input("Enter Num2:\n")

print(f"Sum is {add(number1, number2)}")