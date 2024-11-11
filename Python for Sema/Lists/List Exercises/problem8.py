## Lab Exercise 10/22/2024 Problem 8
## Author: nmessa
## Determine if list is in sorted increasing order

def isIncreasing(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True
    
#Code to test the function
myList1 = [2,4,3,6,8,5,9,9,5,7]
print (myList1)
print (isIncreasing(myList1)) #False

myList2 = [1,2,3,4,4,5,6,7,8,9]
print (myList2)
print (isIncreasing(myList2)) #True

## Output
## [2, 4, 3, 6, 8, 5, 9, 9, 5, 7]
## False
## [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
## True


