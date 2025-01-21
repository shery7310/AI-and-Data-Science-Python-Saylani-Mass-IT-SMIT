# Flatten the following nested dictionary into a single-level dictionary:
# {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

un_flattened_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

''' If I clear the dictionary like this all values and keys of the dictionary will be removed even the copied one in dict_values and dict_keys
dict_values = un_flattened_dict.values()
dict_keys = un_flattened_dict.keys()
un_flattened_dict.clear() 

The reason for this behavior is that dictionary_name.values() and dictionary_name.keys() return a view of the dictionary's keys and values.
A view is not a list or a tuple, although it may look similar. Instead, it is a dynamic reflection of the data currently present in the dictionary.

The variables dict_values and dict_keys hold references to the views returned by un_flattened_dict.values() and un_flattened_dict.keys() rather than independent copies.
As a result, any changes to the original dictionary are immediately reflected in these views.

To make dict_values and dict_keys independent of the dictionary, they can be converted to a tuple or a list, as needed. '''

dict_values = tuple(un_flattened_dict.values()) # this holds {'b': 1, 'c': 2} and {'e': 3, 'f': 4}
dict_keys = tuple(un_flattened_dict.keys()) # this holds a nd d
un_flattened_dict.clear() # Now this will not alter values and keys in dict_values and dict_keys

for val in dict_values:
    un_flattened_dict.update(val) # Each Value is a dictionary itself, We can pass a dictionary directly to a update method

print(un_flattened_dict) # Outputs: {'b': 1, 'c': 2, 'e': 3, 'f': 4}