import math

#defining the function to calculate the area by taking radius as parameter
def circle_area(radius):
    area = math.pi * radius ** 2
    return area

#taking the radius of the circle as input4
radius = float(input("Enter the radius of the circle: "))

#calculating and displaying the area
print(f"The Area of the circle of radius {radius} is {circle_area(radius):.2f}")