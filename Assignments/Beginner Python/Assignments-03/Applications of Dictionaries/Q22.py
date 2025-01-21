# Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).

numbers = {}
for i in range(1, 6):
    numbers.update({i: i * i})

# Another way to do this is using a dictionary comprehension

squares = {num : (num * num) for num in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# oddly a dictionary comprehension is just like a list comprehension
# where instead of using 1 variable we are using a key value pair separated by :