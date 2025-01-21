# Write a program that asks for an integer and checks
# if it’s divisible by 2, 3, or both.

num = int(input("Enter a number:\n"))

if num % 2 == 0 or num % 3 == 0:
    if num % 2 == 0 and num % 3 == 0:
          print(f"{num} is divisible by both 2 and 3.")
    elif num % 2 == 0 and num % 3 != 0:
          print(f"{num} is divisible by 2 only.")
    else:
          print(f"{num} is divisble by 3 only.")           
else:
     print(f"{num} isn't divisble by either of the numbers.")         
 
          