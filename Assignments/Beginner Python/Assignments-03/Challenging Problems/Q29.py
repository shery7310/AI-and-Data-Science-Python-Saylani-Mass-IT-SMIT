# Create a dictionary comprehension to filter out all keys in
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.

some_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys = some_dict.keys()

filtered_keys = {k: v for k, v in some_dict.items() if v < 3}
print(filtered_keys) # Outputs: {'a': 1, 'b': 2}
# Again we could also do this with filter method