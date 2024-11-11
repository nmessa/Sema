## Lab Exercise 10/22/2024 Problem 3
## Author: nmessa
## This program replaces all even values in a list with 0

def zeroEvens(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = 0
    return lst

##def zeroEvens(lst):
##    for number in lst:
##        if number % 2 == 0:
##            number = 0
##    return lst

#Code to test the function
myList = [1,2,3,4,5,6,7,8,9]
print (myList)
print (zeroEvens(myList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## [1, 0, 3, 0, 5, 0, 7, 0, 9]

