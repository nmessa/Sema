##Lab Exercise 9.26.2023
##Author: nmessa

from myMath import *

#Get radius of sphere and store as a float in variable radius
radius = float(input("Enter the radius of a sphere: "))

#Get length, width, and height of cuboid and store in string temp
temp = input("Enter the length, width, and height of a cuboid(seperated by spaces): ")

#break apart string into the strings length, width, and height
length, width, height = temp.split()

#Convert the strings length, width, and height into float values
length = float(length)
width = float(width)
height = float(height)

#Define coefficients of polynomial
poly = [5, 3.2, 7.1, 0, 6.9]

#define a value for x
x = -13

#Test module functions
print ("Surface area of sphere = ", sphereArea(radius))
print ("Volume of sphere = ", sphereVolume(radius))
print ("Surface area of cuboid = ", cuboidArea(length, width, height))
print ("Volume of cuboid = ", cuboidVolume(length, width, height))
print (polyPrettyPrint(poly), '=', evaluatePoly(poly, x))

##Sample Output
##Enter the radius of a sphere: 4
##Enter the length, width, and height of a cuboid(seperated by spaces): 2 4 6
##Surface area of sphere =  201.06192982974676
##Volume of sphere =  268.082573106329
##Surface area of cuboid =  88.0
##Volume of cuboid =  48.0
##6.9X^4 + 0X^3 + 7.1X^2 + 3.2X^1 + 5X^0 = 198234.2

