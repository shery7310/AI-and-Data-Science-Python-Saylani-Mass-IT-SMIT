# Print the reverse of a given number.

number = int(input("Enter a number:\n"))

for num in str(number)[::-1]:
    print(num, end="")


'''
We can also do this without a loop
print(str(number)[::-1])
'''    
