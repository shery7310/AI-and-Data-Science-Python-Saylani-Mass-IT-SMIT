# Write a program to find the largest of two numbers.

num1 = float(input("Enter First Number:\n"))
num2 = float(input("Enter Second Number:\n"))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("The numbers are equal")        