## Lab Exercise 10/8/2024 Problem 2
## Author: nmessa
## This program demonstrates the use of lists
from random import *

numbers = []

#fill the list
for i in range(10):
    numbers.append(randint(1,100));

#print the list
print ('The list')
print (numbers)

#print the even index values
print ('Even index values')
for i in range(0, 10, 2):
    print (numbers[i],end = ' ')
print()

#print the even elements
print ('Even elements')
for i in range(10):
    if numbers[i] % 2 == 0:
        print (numbers[i], end = ' ')
print()

#print the list in reverse
print ('List in reverse')
for i in range(len(numbers)-1, -1, -1):
    print (numbers[i], end = ' ')
print()

#print the first and last element
print ('First element =', numbers[0])
print ('Last element =', numbers[-1])

