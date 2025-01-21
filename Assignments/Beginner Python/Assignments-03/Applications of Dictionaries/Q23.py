# Write a Python program to remove duplicate values from the dictionary
# {'a': 10, 'b': 15, 'c': 10, 'd': 15}.


some_dict = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

def remove_duplicates():

    dict_keys = tuple(some_dict.keys()) # We are fetching all keys of some_dict dictionary, some_dict.keys() returns dict_keys(['a', 'b', 'c', 'd'])
                                        # We are converting returned dict_keys into a tuple
    dict_values = tuple(some_dict.values()) # Here we are fetching values
    some_dict.clear() # This removes all key-value pairs from some_dict in place
    new_dict = {}
    for item in zip(dict_values, dict_keys): # zip is a built-in function that is used for looping over multiple iterables
        # Here zip helping us iterate over two tuples dict_values and dict_keys
        # We could have used two variable, but we are using 1 variable item this way two values are unpacked as a tuple
        if item[0] in new_dict: # This checks if 10 or 15 are already a key
            continue            # if 10 or 15 are already a key we do not want to update dictionary
                                # This is because i want the first instance of some_dict value to be unique
        new_dict.update({item}) # If we pass a tuple to update it will make the first value a key and the next value a value (dictionary)
    return new_dict
    # The question asks us to remove duplicate values but new_dict after removing duplicates has made keys values and values key we need to change that

returned_dict = remove_duplicates()

def format_dict(ret_dict):
    some_dict = {val : key for val, key in zip(returned_dict.values(), returned_dict.keys())}
    # Here we are using a dictionary comprehension
    # But instead of using 1 loop we are using zip which again can fetch two values from two loops
    # Instead of storing keys and values of returned_dict into two tuples we are directly getting them from dict_values and dict_keys
    # Each key and value are stored in val and key variables and each them a new pair of val: key is added to some_dict
    # This makes key and values returned by returned_dict into values and keys of some_dict
    print(some_dict) # Outputs: {'a': 10, 'b': 15}
    # Since c and d has duplicate values they have been removed

format_dict(returned_dict)
