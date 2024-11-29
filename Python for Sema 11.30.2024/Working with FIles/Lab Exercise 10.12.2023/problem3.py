## Lab Exercise 10/12/2023 Problem 3
## Author: nmessa
## This program will print itself to the screen

#read from a file and read in text
myFile = open('problem3.py', 'r')
lines = myFile.readlines()
myFile.close()

#display the text
for i in range(len(lines)):
    print (lines[i], end = '')
    


