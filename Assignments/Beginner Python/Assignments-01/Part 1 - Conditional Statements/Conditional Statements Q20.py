# Create a program that evaluates if an inputted number is prime.

num = int(input("Enter Any Number:\n"))

if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 11 or num == 13:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print(f"{num} is a prime number.")


'''
These are some prime numbers we can check the code against:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293.
From: https://byjus.com/maths/prime-numbers-from-1-to-1000/

It's ovbious that for the code to be accurate we would need a for loop
But for prime numbers between 1-300 this code works just fine
'''    