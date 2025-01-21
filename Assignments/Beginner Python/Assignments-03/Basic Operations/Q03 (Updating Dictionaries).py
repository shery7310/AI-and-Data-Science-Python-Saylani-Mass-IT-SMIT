# Add a new key city to the student dictionary and set its value to "New York".
# This is a very good resource to learn about updating Key Value pairs of dictionaries:
# https://www.digitalocean.com/community/tutorials/python-add-to-dictionary
# Since methods are removing the same key make sure to comment and uncomment parts of the code
# as required

students = {"name": 'Shehryar', "age": 29, "grade": 'A' }

# One way of adding a new key-Value pair is this:
students['city'] = "New York" # Here we are using an assignment operator to assign value to a key

# Another way of doing this is using .update method:
students.update({'city':'New York'}) # Here we are updating the dictionary and add a new key-value pair

# Remember Merging Two dictionaries and adding values is a different thing:
# We can also use the Merge Operator i.e. Dictionary_1 | Dictionary_2:
city = {'city': 'New York'}
student = students | city
print(student) # This merging returns a new dictionary that we are storing into student dictionary
# This will be output: {'name': 'Shehryar', 'age': 29, 'grade': 'A', 'city': 'New York'}

# We can also use Update Operator i.e. Dictionary_1 |= Dictionary_2
city = {'city': 'New York'}
students |= city # This modifies dictionary in-place instead of returning a new dictionary
                 #  and then us having to save the dictionary
print(students)  # {'name': 'Shehryar', 'age': 29, 'grade': 'A', 'city': 'New York'}