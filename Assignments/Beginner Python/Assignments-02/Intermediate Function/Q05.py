# Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
# GCD is also called Highest Common Factor

def gcd(num1_factors, num2_factors):
    common_factors = []
    for nums in num1_factors:
        for num in num2_factors:
            if nums == num:
                common_factors.append(num)
    return max(common_factors)

def calc_gcd():
    num1 = int(input("Enter First Number:\n"))
    num2 = int(input("Enter Second Number:\n"))
    factors_of_num1 = []
    factors_of_num2 = []

    for num in range(1, num1 + 1):
        if num1 % num == 0:
            factors_of_num1.append(num)

    for count in range(1, num2 + 1):
        if num2 % count == 0:
            factors_of_num2.append(count)

    print(f"The Greatest Common Divisor between {num1} and {num2} is {gcd(factors_of_num1, factors_of_num2)}")
calc_gcd()