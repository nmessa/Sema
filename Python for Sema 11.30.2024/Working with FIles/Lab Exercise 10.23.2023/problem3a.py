#Lab Exercise 10.23.2023 Problem 3a
#Author: nmessa
#This program will read lines from the coefficents of a quadratic
#equation from a file coefficients.txt.  The program will find the
#roots of the equation and write them back to roots.txt
#This version handles complex number roots

from random import *
from math import *
DATA_SIZE = 1000000
##Generates coefficients file
##outFile = open('coefficients.txt', 'w')
##count = 0
##while count < DATA_SIZE:
##    a = randint(-100, 100)/10
##    b = randint(-100, 100)/10
##    c = randint(-100, 100)/10
##    if a != 0:
##        outFile.write(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
##        count += 1
##outFile.close()

#Open file to read
inFile = open("coefficients.txt", "r")

#read all lines and store in list lines
lines = inFile.readlines()

#close the file
inFile.close()

#open a file to write
outFile = open("roots2.txt", "w")

#process each line from the file
for line in lines:
    numbers = line.split()
    a = float(numbers[0])
    b = float(numbers[1])
    c = float(numbers[2])
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + sqrt(discriminant))/(2*a)
        root2 = (-b - sqrt(discriminant))/(2*a)
        outFile.write(str(round(root1,3)) + ' ' + str(round(root2,3)) + '\n')
    else:
        real1 = -b/(2*a)
        complex1 = sqrt(-discriminant)/(2*a)
        real2 = -b/(2*a)
        complex2 = -sqrt(-discriminant)/(2*a)
        outFile.write(str(round(real1,3)) + ' ' + str(round(complex1,3)) + 'i  '
                      + str(round(real2,3)) + ' ' + str(round(complex2,3))+ 'i\n')
#close the file
outFile.close()
