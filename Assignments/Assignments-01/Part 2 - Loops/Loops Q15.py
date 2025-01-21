# Print the sum of even and odd numbers separately up to a given number.

num = int(input("Enter a number:\n"))
sum_even = 0
sum_odd = 0

print("\n")
for number in range(1, num):
    if number % 2 == 0:
        sum_even += number
    elif number % 2 != 0:
        sum_odd += number   
print("\n")
print(f"Even Number Sum is: {sum_even}")
print(f"Odd Number Sum is: {sum_odd}")     