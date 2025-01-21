''' Take three sides of a triangle as input and check if they form a valid triangle.
The sum of any two sides of a triangle is greater than or equal to the third side
according to Triangle Inequality Theorem from Euclidean geometry.

https://www.youtube.com/watch?v=BiagrTl2y4o

To form a valid triangle
all three of the following conditions must be satisfied:

side1 + side2 > side3
side2 + side3 > side1
side3 + side1 > side2

For example:

3 + 4 > 5
4 + 5 > 3
3 + 5 > 4
'''


side1 = input("Enter Side1 Length:\n")
side2 = input("Enter Side2 Length:\n")
side3 = input("Enter Side3 Length:\n")

side1, side2, side3 = float(side1), float(side2), float(side3)

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("This is a valid Triangle")
else:
    print("According to Triangle Inequality Theorem\nThis wouldn't be a valid triangle")

''' We could also nest this condition i.e.
The above code block and this one that I commented are the same
if side1 + side2 > side3:
    if side2 + side3 > side1:
        if side1 + side3 > side2:
            print("This is a valid Triangle")
else:
    print("According to Triangle Inequality Theorem\nThis wouldn't be a valid triangle")
    '''            