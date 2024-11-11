## Lab Exercise 10/22/2024 Problem 5
## Author: nmessa
## This program removes the middle of the list
## If the length of the list is odd remove the middle element
## If the length of the list is even remove the middle two elements

def removeMiddle(lst):
    if len(lst) % 2 == 1:
        lst.remove(lst[len(lst)//2])
        return lst
    else:
        lst.remove(lst[len(lst)//2])
        lst.remove(lst[len(lst)//2])
        return lst
        

#Code to test the function
oddList = [1,2,3,4,5,6,7,8,9]
print (oddList)
print (removeMiddle(oddList))
evenList = [1,2,3,4,5,6,7,8,9,10]
print (evenList)
print (removeMiddle(evenList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## [1, 2, 3, 4, 6, 7, 8, 9]
## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## [1, 2, 3, 4, 7, 8, 9, 10]

