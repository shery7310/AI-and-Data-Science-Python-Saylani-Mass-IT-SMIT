# Create a program that simulates a countdown timer 
# starting from a given number down to zero.

num = int(input("Enter a starting number:\n"))
end = 1
for num in range(num, end, -1):
    print(num)

# Try starting the counter with something like 1000000    