# Create a function that takes a list of integers and returns the sum of all even numbers.
integers = input("Input Integers separated by space:\n").split(" ")
even_nums = [int(num) for num in integers if (int(num) % 2 == 0)]
def sum_of_evens(numbers):
    add = 0
    for num in even_nums:
        add += num
    print(f"The sum if all even numbers is: {add}")
sum_of_evens(even_nums)