# Print the multiplication table of a given number.

num = int(input("Enter Number you want a table for:\n"))

if num > 1:
    counter = 1
    while counter != 11: # as soon as counter reaches 11 and loop will break
        print(f"{num} x {counter} = {num * counter}")
        counter += 1