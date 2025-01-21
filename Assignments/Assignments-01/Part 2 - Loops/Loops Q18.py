# Use a loop to print numbers in reverse order within a given range.

print("We want to print the given number in reverse order")


number = int(input("Enter a number:\n"))
start = int(input("Enter The Value you want to start range from:\n"))
end = int(input("Enter The Value you want to end range on:\n"))

for num in str(number)[start:end:-1]:
    print(num, end="")