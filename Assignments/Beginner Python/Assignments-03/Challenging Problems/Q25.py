# Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7},
# write a Python program to add the values of matching keys and print the result.

dict1 = {'a': 5, 'd': 12, 'b': 10, 'e': 9}
dict2 = {'c': 19,'a': 3, 'b': 7, 'e': 29}

def add_dicts(dict1, dict2): # Here in definition two sets are arguments that add_dicts expects
    keys_dict1_set = set(dict1.keys()) # This fetches all the keys of dict1 and will only keep unique keys from dict1 and converts the list to a set
    keys_dict2_set = set(dict2.keys()) # We converted these into a set because we want to use intersection function/operator of sets
                                       # Intersection means common elements in both sets
                                       # When we take intersection of two sets a new set of common_keys is returned having only common values that are in both sets
    common_keys = keys_dict1_set & keys_dict2_set
    # Another way of intersection is:
    # common_keys = keys_dict1_set.intersection(keys_dict2_set)
    # This set contains a, b and e keys

    for key in common_keys: # This loop runs 3 times but each time we are fetching values of dict1 and dict2 of the keys present in common_keys
        print(f"Value of {key} in dict1 is {dict1[key]} and value of {key} in dict2 is {dict2[key]}")
        print("So sum of the values is:", dict1[key] + dict2[key])

add_dicts(dict1, dict2)