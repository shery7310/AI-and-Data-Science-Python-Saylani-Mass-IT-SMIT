# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
# This is syntax of any dictionary:
# dict_name = {key: value()} the Values can be anything i.e. string, number, list, tuple, set etc


student_names = ['Hanzala', 'Shehryar', 'Hamza', 'Bilal', 'Ali']
student_ages = [22, 29, 21, 24, 25]
student_grades = ['B', 'A', 'C', 'A', 'B']

students = {"name": student_names, "age": student_ages, "grade": student_grades }

# student_comp = [student for student in students] Such a List Comprehension fetches keys
student_comp = [student for student in students.values()] # this will fetch values and make them nest

for val in student_comp:
    print(val) # This will return three separate lists as inside the comprehension these were part of nested lists