##Lab Exercise 9.26.2023
##Author: nmessa
import myMath

#Get radius of sphere and stroe as a float in variable radius
radius = float(input("Enter the radius of a sphere: "))

#Get length, width, and height of cuboid and store in string temp
temp = input("Enter the length, width, and height of a cuboid: ")

#Alternate input
##length = input("Enter the length of a cuboid: ")
##width = input("Enter the width of a cuboid: ")
##height = input("Enter the height of a cuboid: ")

#break apart string into the strings length, width, and height
length, width, height = temp.split()

#Convert the strings length, width, and height into float values
length = float(length)
width = float(width)
height = float(height)

#Define coefficients of polynomial
#6.9X^4 + 7.1X^2 + 3.2X + 5 = 0
poly = [5, 3.2, 7.1, 0, 6.9]

#define a value for x
x = -13

#Test module functions
print ("Surface area of sphere = ", myMath.sphereArea(radius))
print ("Volume of sphere = ", myMath.sphereVolume(radius))
print ("Surface area of cuboid = ", myMath.cuboidArea(length, width, height))
print ("Volume of cuboid = ", myMath.cuboidVolume(length, width, height))
print (myMath.polyPrettyPrint(poly), '=', myMath.evaluatePoly(poly, x))

##Sample Output
##Enter the radius of a sphere: 4
##Enter the length, width, and height of a cuboid: 2 4 6
##Surface area of sphere =  201.06192982974676
##Volume of sphere =  268.082573106329
##Surface area of cuboid =  88.0
##Volume of cuboid =  48.0
##6.9X^4 + 0X^3 + 7.1X^2 + 3.2X^1 + 5X^0 = 198234.2


