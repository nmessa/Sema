## Lab Exercise 10/22/2024 Problem 10
## Author: nmessa
## Determine if list has duplicates

def hasDups(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False
    
#Code to test the function
myList1 = [2,4,3,6,8,5,9,7,5,7]
print (myList1)
print (hasDups(myList1)) #True

myList2 = [1,2,3,4,5,6,7,8,9]
print (myList2)
print (hasDups(myList2)) #False

## Output
## [2, 4, 3, 6, 8, 5, 9, 7, 5, 7]
## True
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## False


