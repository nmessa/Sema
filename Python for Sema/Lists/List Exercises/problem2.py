## Lab Exercise 110/22/2024 Problem 2
## Author: nmessa
## This program shifts the list right with wrap around

def shiftRight(lst):
    temp = lst[-1]
    for i in range(len(lst)-2, -1, -1):
        lst[i+1] = lst[i]
    lst[0] = temp
    return lst

#Code to test the function
myList = [1,2,3,4,5,6,7,8,9]
print (myList)
print (shiftRight(myList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## [9, 1, 2, 3, 4, 5, 6, 7, 8]

