# Write a function to calculate the area of a circle given its radius.
rad = float(input("Enter Radius:\n"))
def area_circle(radius):
    pi = 3.14
    area = radius * pi
    return area

print(area_circle(3))