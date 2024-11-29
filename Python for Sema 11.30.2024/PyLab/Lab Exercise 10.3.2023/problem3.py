## Lab Exercise 10/3/2023 Problem 3
## Author: nmessa
## This program will plot a function using pylab
from pylab import *

#Define a function f(x) = 0.00005X^3 - 0.03X^2 +4X +200
def f(x):
   return 0.00005 * x**3 - 0.03*x**2 + 4 * x + 200

#Create 2 lists to hold the x and y values
xVals = []
yVals = []

#Build the lists
for x in range(400):
    xVals.append(x)
    yVals.append(f(x))

#Plot the data
plot(xVals, yVals)
grid(True)
show()


    
