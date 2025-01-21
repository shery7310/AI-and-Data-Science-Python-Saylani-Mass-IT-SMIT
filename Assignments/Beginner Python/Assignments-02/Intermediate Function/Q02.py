num = int(input("enter Nth Number\n"))
# Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 55
# we are staring indexing with 0 as first two numbers in fibonacci series are 0 and 1
# indexes           0 1 2 3 4 5 6 7  8  9  10

def rec_fibonacci(nth):
    if nth == 0 or nth == 1: # this is the base case
        return nth
    # If nth is greater than 1, it is computed as the sum of the two preceding Fibonacci numbers: fibonacci(nth - 1) and fibonacci(nth - 2)
    return rec_fibonacci(nth - 1) + rec_fibonacci(nth - 2)

"""For example, if nth = 3, the function will call rec_fibonacci(2) and rec_fibonacci(1).
The result of rec_fibonacci(2) will be computed recursively,
while rec_fibonacci(1) directly hits the base case and returns 1. """

print(rec_fibonacci(num))
