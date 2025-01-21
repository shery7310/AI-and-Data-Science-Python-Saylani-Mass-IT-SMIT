''' Ask the user for a grade percentage and display the corresponding
 letter grade (A, B, C, D, F)

A-Grade Range (80(inclusive) - 100(inclusive))
B-Grade Range (70(inclusive) - 80(exclusive))
C-Grade Range (60(inclusive) - 70(exclusive))
D-Grade Range (50(inclusive) - 60(exclusive)) 
Below 50 Fail
'''

grade_percentage = float(input("Enter You Grade Percentage:\n"))
grade_percentage = round(grade_percentage)

if grade_percentage >= 80 and grade_percentage <=100:
    print("You scored an A Grade, Congrats!")
elif grade_percentage >= 70 and grade_percentage < 80:
    print("You scored a B Grade, There was room for improvement!")
elif grade_percentage >= 60 and grade_percentage <70:
    print("You scored an C Grade, Come on Man!")
elif grade_percentage >= 50 and grade_percentage < 60:
    print("You scored a D Grade, Goodluck Explaining this to your Parents!")
elif grade_percentage < 50:
    print("You have failed, You had one job!")
else:
    print("Enter Valid Grade Percentage!!!")
