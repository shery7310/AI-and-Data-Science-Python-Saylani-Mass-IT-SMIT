# Check if the key grade exists in the student dictionary and print True or False.
students = {
    "names": ['Shehryar', 'Hassan', 'Adeel', 'Nabeel', 'Mudassar', 'Mubasshar', 'Aqeel'],
    "ages": [29, 24, 21, 25, 30, 23, 24],
    "grades": ['A', 'B', 'A', 'C', 'B', 'A', 'D'] }

print(True if 'grades' in students else False) # This Ternary Operator implementation in python
# It means print True if 'grades' is in students dictionary else print False
