## Lab Exercise 10.16.2023 Problem 4
## Author: nmessa
## This program will find the average of two data sets
from random import *

#This is the code I used to generate the data
#generate 1000000 sets of random integer data in two columns
##myFile = open('numbers.dat', 'w')
##for i in range(1000000):
##   r1 = randint(1, 10000)
##   r2 = randint(1, 10000)
##   myFile.write(str(r1) + ' ' +str(r2) + '\n')
##myFile.close()

#Create 2 empty lists to hold data from column 1 and column 2
nums1 = []
nums2 = []

#read data in
myFile = open('numbers.dat', 'r')
lines = myFile.readlines()
myFile.close()

#process each line and add the values to column 1 and column 2 list
for line in lines:
   values = line.split()
   nums1.append(int(values[0]))
   nums2.append(int(values[1]))

#calculate the average
average1 = sum(nums1)/len(nums1)
average2 = sum(nums2)/len(nums2)

print ("The average of column 1 =", round(average1, 2))
print ("The average of column 2 =", round(average2, 2))

## Output with my dataset
## The average of column 1 = 4996.16
## The average of column 2 = 5004.47

   
