# Write a function that calculates the power of a number without using the ** operator.

def calculate_power():
    num = int(input("Enter a number:\t"))
    print()
    power = int(input("Enter a number:\t"))
    print()
    result = 1

    for _ in range(1, power + 1):
        result *= num
    print(f"{num}^{power} = {result}")

calculate_power()
