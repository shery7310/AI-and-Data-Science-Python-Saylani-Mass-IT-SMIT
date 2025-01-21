''' 
Take two numbers and an operator (+, -, *, /) as input and perform
the corresponding operation. '''

num1 = float(input("Enter 1st Number:\n"))
num2 = float(input("Enter 2nd Number:\n"))
print("\n")

print("What do you want to do with these numbers:\nEnter +, -, * or / only:\t")
operation = input("\n")

if operation == '+':
    print(f"sum = {num1 + num2}")
elif operation == '-':
    print(f"difference = {num1 - num2}")
elif operation == '/':
    print(f"division = {num1 / num2}")
elif operation == '*':
    print(f"product = {num1 * num2}")
else:
    print(f"Enter a valid symbol\nYou entered: {operation}")