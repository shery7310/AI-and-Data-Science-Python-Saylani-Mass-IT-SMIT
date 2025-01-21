# Take the length of three sides and classify the triangle
''' (equilateral, isosceles, or scalene).
In case of Equilateral Triangle all sides must be equal
For Isosceles any two sides must be equal
For Scalene no need for any equal side.

'''

length1 = int(input("Enter Side 1 Length:\n"))
length2 = int(input("Enter Side 2 Length:\n"))
length3 = int(input("Enter Side 3 Length:\n"))

if length1 == length2 == length3:
    print("This is an Equilateral Traingle.")
elif length1 == length2 or length2 == length3 or length3 == length1:
    print("This is an Isosceles Triangle.")
else:
    print("This is a Scalene Triangle") 