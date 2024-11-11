## Lab Exercise 10/9/2024 Problem 2
## Author: nmessa
## This program generates 10 permutations of the numbers 1 to 10
from random import *

#Create an empty list to hold permutations
permutations = []

#Create a list to hold integers 1 to 10
numbers = [1,2,3,4,5,6,7,8,9,10]

#Generate 10 lists of permutations of numbers 1 to 10
for p in range(10):
    for i in range(10):
        n = choice(numbers)
        permutations.append(n)
        numbers.remove(n)
    print (permutations)
    #reset permutation and number list
    permutations = []
    numbers = [1,2,3,4,5,6,7,8,9,10]

##Sample output
##[10, 1, 2, 4, 8, 3, 5, 9, 7, 6]
##[8, 9, 5, 4, 2, 10, 6, 1, 7, 3]
##[2, 3, 8, 5, 7, 9, 6, 10, 4, 1]
##[1, 9, 10, 3, 8, 4, 6, 5, 7, 2]
##[8, 1, 7, 3, 4, 6, 9, 5, 10, 2]
##[3, 10, 8, 6, 4, 7, 2, 5, 1, 9]
##[4, 2, 3, 9, 1, 10, 5, 8, 7, 6]
##[6, 5, 10, 9, 7, 1, 8, 3, 2, 4]
##[10, 3, 2, 7, 9, 4, 1, 5, 8, 6]
##[7, 5, 10, 8, 2, 1, 4, 9, 6, 3]

