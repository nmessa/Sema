#MyPow.py
#Author: nmessa
#Date: 10.27.2023

from math import *

#Get user input
x = float(input("Enter the value for X: "))
y = float(input("Enter the value for Y: "))

#Calculate X**Y
answer = exp(y * log(x))

print("The result from using the formula is:", answer)
print("The result from using the Math pow functtion is: ", pow(x, y))

##Sample Output
##Enter the value for X: 7
##Enter the value for Y: 5
##The result from using the formula is: 16806.99999999998
##The result from using the Math pow functtion is:  16807.0
