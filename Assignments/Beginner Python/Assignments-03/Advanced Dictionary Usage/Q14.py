# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.

some_dict = {'a': 1, 'b': 2, 'c': 3}
li_tuples = []
for key_value in some_dict.items():
    li_tuples.append(key_value) # We are unpacking each key-value pair as a tuple and appending to an empty list
                                # Since tuples are immutable we can not sort them that's why we are using a list

li_tuples.sort(reverse=True) # This sorts list in place in descending order
print(li_tuples) # outputs: [('c', 3), ('b', 2), ('a', 1)]
some_dict.clear() # we remove all elements inside the dict
some_dict.update(li_tuples) # Then we give the list of tuples to the update method of dictionaries
print(some_dict) # outputs: [('c', 3), ('b', 2), ('a', 1)]