# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

dict1 = {'c': 3, 'b': 2, 'a': 1}
dict2 = {'a': 1, 'd': 4, 'e': 5, 'c': 3, 'b': 2}
dict3 = dict1 | dict2 # We can see that keys in dict1 are already present in dict2 in this case keys of dict2 take precedence
                      # as dict2 comes last

def check_identical_dicts(first_dict, second_dict):
    if first_dict == second_dict:
        print('Yes they are identical')
    else:
        print("Nope! these are not identical")

check_identical_dicts(dict2, dict3)

print(dict2) # outputs: {'a': 1, 'd': 4, 'e': 5, 'c': 3, 'b': 2}
print(dict3) # outputs: {'c': 3, 'b': 2, 'a': 1, 'd': 4, 'e': 5}
# Since dictionaries are implementation of hashtable order does not matter in their case
# Because check_identical_dicts is actually comparing keys and their respective values