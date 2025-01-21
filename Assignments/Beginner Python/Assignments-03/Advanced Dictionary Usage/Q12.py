# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
user_info = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]

user_dict = {}
user_dict.update(user_info) # The update method for dictionaries allows us to pass tuple
# The function automatically made the first of a tuple key and the second value the value of that key
print(user_dict) # {'name': 'Alice', 'age': 25, 'city': 'Paris'}

# We can add this tuple to the dictionary this way:
another_user_dict = {}
for key_value in user_info:
    another_user_dict.update({key_value[0]: key_value[1]})
print(another_user_dict)