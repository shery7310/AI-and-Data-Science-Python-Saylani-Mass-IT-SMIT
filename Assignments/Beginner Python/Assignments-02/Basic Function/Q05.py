# Create a function to check if a given number is prime.

import math # importing to use sqrt

primes = []
def value_has_decimal(value):
    after_decimal, number = math.modf(value) # the functions returns both decimal value and number separately
    # if after_decimal = 0.2243000000000004 ceil will convert it to 1
    if after_decimal > 0: # for example (0.35, 5)
        number = math.ceil(number)
        return after_decimal, number
    else:
        return after_decimal

def is_prime(num: int) -> str:
    check = ''
    if num <= 1:
        return f"{num} is not a prime."
    elif num == 2 or num == 3:
        return f"{num} is a prime."
    elif num > 3:
        num_sqrt = math.sqrt(num) # 11
        upper_range = math.ceil(num_sqrt) # 4
        if value_has_decimal(num_sqrt) == 0:
            return f"{num} is not a prime."
        lower_range = value_has_decimal(num_sqrt)[1]
        for i in range(upper_range, 1, -1):
            if num % i == 0:
                check = 0
                break
        if check == 0:
            return f"{num} is not prime number"
        else:
            primes.append(num)
            return f"{num} is a prime number"

print(is_prime(num := int(input("Enter a number:\n"))))
# here we are using a walrus operator that will input and feed it to is_prime function