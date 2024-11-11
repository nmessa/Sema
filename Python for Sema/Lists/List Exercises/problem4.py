## Lab Exercise 10/22/2024 Problem 4
## Author: nmessa
## This program replaces all elements in the list (except first and last
## elements) with the larger neighbor

def replaceLargerNeighbor(lst):
    for i in range(1, len(lst)-1):
        lst[i] = max(lst[i-1], lst[i+1])
    return lst


#Code to test the function
myList = [1,2,3,4,5,8,7,9]
print (myList)
print (replaceLargerNeighbor(myList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## [1, 3, 4, 5, 6, 7, 8, 9, 9]




