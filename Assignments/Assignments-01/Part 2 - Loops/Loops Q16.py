# Create a program to calculate the sum of the digits of an inputted integer.

nums = int(input("Enter a number:\n"))

sum = 0
for num in str(nums): 
    sum += int(num)
print(f"The sum is: {sum}")