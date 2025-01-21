# Write a program that checks if a given number is positive, negative, or zero.

num = float(input("Enter any number:\n"))

if num > 0:
    print(f"{num} is a Postive Number")
elif num < 0:
    print(f"{num} is a Negative Number")    
else:
    print(f"This number is 0")