# Remove the key city from the student dictionary.
# Since methods are removing the same key make sure to comment and uncomment parts of the code
# as required

student = {'name': 'Shehryar', 'age': 29, 'grade': 'A', 'city': 'New York'}

# We can remove a Key-Value pair using del keyword and the key we want to remove
del student['city']
# print(student) # Outputs: {'name': 'Shehryar', 'age': 29, 'grade': 'A'}

# Another way is to use .pop() method and pass it a key, we can not use it without passing a key:
student.pop('city') # Will remove Key-Value pair for key city, we can also set a default value for popping

# Another way is using .popitem() This doesn't expect an argument and will remove the last most recent key-value pair inserted
student.popitem()

# This will remove the clear all key-value pairs inside dictionary:
student.clear()

# This deletes the entire dictionary
del student