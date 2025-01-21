# Access the value of the key grade in the student dictionary.
name = ['Hanzala', 'Shehryar', 'Hamza', 'Bilal', 'Ali']
age = [22, 29, 21, 24, 25]
grade = ['B', 'A', 'C', 'A', 'B']

students = {"name": name, "age": age, "grade": grade }

# print(students['grade']) # Outputs: ['B', 'A', 'C', 'A', 'B']
# To access Let's say Grade of Shehryar we can:
for val in students.values(): # Unpacks each value of dictionary in each iteration
    if 'Shehryar' in val: # checks if name 'Shehryar' is in the dictionary
        print(students['grade'][1]) # Since Shehryar's grade is at index 1 in grade list therefore we access that specific grade
                                    # We access a dictionary by its keys 'grade' is a key
