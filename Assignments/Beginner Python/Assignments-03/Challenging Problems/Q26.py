# Write a Python program to create a dictionary where the keys are the first
# n positive integers, and the values are their cubes. Take n as user input.


# Here, I am assuming that the instructor wants the user to specify how many elements (key-value pairs)
# should be included in the dictionary.
n = int(input("Enter A Positive Integer Till which you want elements in the dictionary:\n"))

def create_dict(input_value):
    if n <= 0:
        return "No Key Value Elements Possible for given number"
    else:
        cubes_till_n = {num : (num * num * num) for num in range(1, input_value + 1)} # This will keep on making num
        # a key till the number entered by the user is reached, and for value each of that num is multiplied thrice
        # so that a cubes are found and set as values
        return cubes_till_n

print("Here's the dictionary", create_dict(n))