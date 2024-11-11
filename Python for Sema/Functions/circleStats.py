##circleStats.py
##Author: nmessa
##Date: 12.4.2023
##This program allows the user to enter the radius of a circle an
##displays the diameter, circumference, and area

from math import pi

def diameter(r):
    d = 2 * r
    return d

def circumference (r):
    circ = 2 * pi * r
    return circ

def area (r):
    a = pi * r * r
    return a

#Get user input
radius = float(input("Enter the readius of a circle: "))

#Call 3 functions and pass radius to each
theDiameter = diameter(radius)
theCircumference = circumference(radius)
theArea = area(radius)

#Print results
print("Diameter =", theDiameter)
print("Circumference =", theCircumference)
print("Area =", theArea)

##Sample Output
##Enter the readius of a circle: 1
##Diameter = 2.0
##Circumference = 6.283185307179586
##Area = 3.141592653589793
