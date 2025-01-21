# Use a for loop to print each character of a string.
string = input("Enter any string:\n")

for char in string:
    print(char)

'''
We can also achieve this using while loop like this:
runs = 0
while runs != len(string):
    print(string[runs])
    runs += 1  
'''