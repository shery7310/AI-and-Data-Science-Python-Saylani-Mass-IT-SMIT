# Check if a given number is a multiple of both 3 and 5.

num = int(input("Enter Any Number:\n"))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is a multiple of 3 and 5")