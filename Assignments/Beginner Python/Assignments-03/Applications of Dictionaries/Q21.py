# Write a Python program to find the key with the maximum value in the dictionary
# {'a': 10, 'b': 15, 'c': 7}.

numbers_dict = {'a': 10, 'b': 15, 'c': 7}
maximum_value = max(numbers_dict.values()) # number_dict.values returns something like a dictionary tuple i.e. dict_values([10, 15, 7])
print(maximum_value) # We used built in method max to find the maximum value in a tuple