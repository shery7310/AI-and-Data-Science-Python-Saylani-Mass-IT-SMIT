# Write a program to check if a number is within a specified range.


print("Specify a range", "Enter a minimum value and a maximum value when asked:\n")

minimum = int(input("Enter Minimum Number:\n"))
maximum = int(input("Enter Maximum Number:\n")) 
num = int(input("Enter a number:\n"))


if minimum > maximum:
    print("The maximum needs to be larger than minimum.")
elif num >= minimum and num <= maximum:
    print(f"Yes {num} is in the specified range.")
elif minimum == maximum:
    print("There can be no integer within this range.")    

''' A very different logic could have been:
range() in python is just like a sequence of numbers of range object
So when we check if this number is in the range it returns True if
The number is actually there

elif num in range(minimum, maximum):
    print(f"Yes {num} is in the specified range.") '''