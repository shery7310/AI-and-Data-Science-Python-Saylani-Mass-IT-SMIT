# Print all odd numbers between 1 and 100 using a loop.

num = 1
while num < 101:
    if num % 2 != 0:
        print(num, end=" ") 
    num += 1

'''
It seems we can also get odd numbers by adding 2 to the previous ones
we can do that using this logic:
'''

# counter = 1
# while counter < 101:
#     print(counter, end=" ")
#     counter += 2