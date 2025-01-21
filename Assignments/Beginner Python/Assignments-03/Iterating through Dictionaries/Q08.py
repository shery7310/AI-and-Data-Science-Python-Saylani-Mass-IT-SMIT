# Iterate through the dictionary student and print all key-value pairs in the format key: value.
students = {
    "names": ['Shehryar', 'Hassan', 'Adeel', 'Nabeel', 'Mudassar', 'Mubasshar', 'Aqeel'],
    "ages": [29, 24, 21, 25, 30, 23, 24],
    "grades": ['A', 'B', 'A', 'C', 'B', 'A', 'D'] }

for student, student_value in students.items(): # .items is unpacking both keys and values
    print(f"{student} : {student_value}")

# To unpack individual student data we can:

for student_no in range(len(students["names"])): # By using students["names"] we are accessing a list of names student_no contains the current
                                                 # index we want to run the internal loop the times the students because we want data for each student
    student_data = "Student's Name: "            # This is a string that is re-assigned after internal loop runs for each key, value pairs


    for student, student_value in students.items(): # Keys and Their values are being unpacked in variables student and student_value
        if student == 'names':                      # When key is names we want to access the list element at current index i.e. 0, 1, 2,..
            student_data += student_value[student_no] # Student's Name is concatenated to the string
            student_data += " Student's Age: " # Then we concatenate space + "Student's Age: " to student_data string
        elif student == 'ages':  # When key is ages we want to access the list element at current index i.e. 0, 1, 2,..
            student_data += str(student_value[student_no]) # Since elements inside this list are int we need to convert them to string as we are concatenating to a string
            student_data += " Student's Grade: " # Again We concat another string to student_data
        elif student == 'grades': # When key is grades we now want to concatenate the grade for the current student
            student_data += student_value[student_no]
                                  # internal for loop ends here and the flow exits it because next line is part of outerloop
    print(student_data) # This prints Student's Name: Shehryar Student's Age: 29 Student's Grade: A for first iteration of outer_loop

# There is an easier way to do this: (And this is the better logic utilizing dictionaries features)
print("------------------------------------------------------------------")
for student_no in range(len(students["names"])):
    print(f"Student's Name: {students['names'][student_no]} Student's Age: {students['ages'][student_no]} Student's Grade: {students['grades'][student_no]}")
