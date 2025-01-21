# Merge the following two dictionaries and print the result: dict1 = {'a': 1, 'b': 2}, dict2 = {'c': 3, 'd': 4}.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict_merged = dict1 | dict2 # The merge operator returns a new dictionary after merging so we are storing the returned dictionary
                            # new dictionary means new memory address
print(dict_merged) # outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# We can also update operator the dictionaries in-place using:

dict1 |= dict2
print(dict1) # This way the dictionary at left-hand side is merged with 2nd dictionary but in place