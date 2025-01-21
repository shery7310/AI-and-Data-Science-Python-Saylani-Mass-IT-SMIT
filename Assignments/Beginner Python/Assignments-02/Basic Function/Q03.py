# Write a function to find the factorial of a number using recursion.
num = int(input("enter num:\n"))

''' Equivalent Loop Structure
fact = num
for i in range(num - 1, 1, -1):
    fact *= i
'''

def rec_fact(number):
    if number == 1:
        return 1
    
    return number * rec_fact(number - 1)

print(rec_fact(num))