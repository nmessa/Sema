## Lab Exercise 10/22/2024 Problem 1
## Author: nmessa
## This program swaps the first and last element in a list

def swapFirstAndLast(lst):
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp
    return lst

#Code to test the function
myList = [1,2,3,4,5,6,7,8,9]
print (myList)
print (swapFirstAndLast(myList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## [9, 2, 3, 4, 5, 6, 7, 8, 1]
