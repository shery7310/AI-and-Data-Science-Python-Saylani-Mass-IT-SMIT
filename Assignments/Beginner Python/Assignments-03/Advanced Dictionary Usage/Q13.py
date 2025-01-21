# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.

some_dict = {'z': 1, 'a': 2, 'c': 3}

dict_li = []
for key_value in some_dict.items(): # instead of unpacking both key and value separately
                                    # I am unpacking both in 1 variable
    dict_li.append(key_value)       # the variable key_value holds a tuple of the key-value pair
                                    # each tuple is appended to the dict_li list
                                    # now we need to sort this list of tuples

dict_li.sort()                     # this sorts list in place
some_dict.clear()                  # Now we need to recreate the dictionary, some_dict is now empty

some_dict.update(dict_li)          # The list of tuples have been added to the dictionary
print(some_dict)                   # outputs: {'a': 2, 'c': 3, 'z': 1}