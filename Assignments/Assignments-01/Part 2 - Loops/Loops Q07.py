# Find the factorial of a number using a while loop.

num = int(input("Enter Any Number:\n"))

counter = 2 # starting from 2 so multiplying actually starts from 2 instead of 1 
fact = 1
while counter < num + 1: # for example user entered 5, this will multiply like 1 x 2 x 3 x 4 x 5 which is 120
    fact *= counter
    counter += 1

print(f"The factorial is: {fact}") 



'''
Here's how we can achieve the same thing iterating reversely i.e. 5, 4, 3, 2, 1...

factu = 1
count = num -1
while count > 1:
    factu *= count
    count -= 1  

print(f"The factorial is: {factu*num}")
Such Code must always be dry-run    
 '''


