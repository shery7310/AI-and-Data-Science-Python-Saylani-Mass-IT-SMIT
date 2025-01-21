# Print all prime numbers between 1 and 50.
'''
A prime number has only 2 factors
Whereas a non prime number has more than 2 factors
'''

factors = []

number = int(input("Enter any integer:\n"))

for elem in range(1, number + 1):
    if number % elem == 0:
        factors.append(elem)

if len(factors) == 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")   

# We can also do this without a list using a counter

'''
number = int(input("Enter any integer:\n"))
counter = 0
for elem in range(1, number + 1):
    if number % elem == 0:
        counter += 1

if counter == 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
'''       