# Iterate through the dictionary student and print all values.

students = {
    "names": ['Shehryar', 'Ali', 'Adeel', 'Nabeel', 'Mudassar'],
    "ages": [29, 24, 21, 25, 30],
    "grades": ['A', 'B', 'A', 'C', 'B']
}

for student in students.values():
    print(student) # This sequentially accesses the values of the keys which are lists