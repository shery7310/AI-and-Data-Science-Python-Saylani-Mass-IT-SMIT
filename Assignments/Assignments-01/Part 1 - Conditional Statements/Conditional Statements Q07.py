# Write a program to find the largest of three numbers.

num1 = float(input("Enter First Number:\n"))
num2 = float(input("Enter Second Number:\n"))
num3 = float(input("Enter Third Number:\n"))

if num1 == num2 == num3:
    print(f"All the numbers are equal")
elif num1 == num2:
    if num3 > num1:
        print(f"{num3} is the greatest number")
    else:
        print("Number-1 and Number-2 are greater")
elif num2 == num3:
    if num1 > num2:
        print(f"{num1} is the greatest number")
    else:
        print("Number-2 and Number-3 are greater")
elif num3 == num1:
    if num2 > num1:
        print(f"{num2} is the greatest number")
    else:
        print("Number-3 and Number-1 are greater")
else:
    # both implementations are essentially the same
    # if num2 > num3 > num1:
    #     print(f"{num2} is the greatest number")
    # elif num3 > num2 >num1:
    #     print(f"{num2} is the greatest number")
    # elif num1 > num2 >num3:
    #     print(f"{num2} is the greatest number")

    if num2 > num3 and num2 > num1:    
        print(f"{num2} is the greatest number")
    elif num3 > num2 and num3 > num1:
        print(f"{num3} is the greatest number")
    elif num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest number")    






'''
We could have taken input from user in a single line using a list

nums = []
nums = input("Enter Numbers seperated by comma:\n").split(",")
# but the elements of the list currently are strings     '''    