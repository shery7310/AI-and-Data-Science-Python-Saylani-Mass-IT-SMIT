# Use a loop to count the number of digits in an integer.

nums = int(input("Enter any integer:\n"))

counter = 0
for num in str(nums): # for example number is 123
    counter+=1 # num = 1 in first iteration and counter is incremented to 1
print(counter) # then counter is incremented to 2 when num = 2
               # then counter is incremented to 3 when num = 3

# This could be done in easier way using built-in python functions i.e.
# print(len(str(nums)))
