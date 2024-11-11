## Lab Exercise 10/22/2024 Problem 9
## Author: nmessa
## Determine if list has adjacent duplicate

def adjacentDups(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False
    
#Code to test the function
myList1 = [2,4,3,6,8,5,9,7,5,7]
print (myList1)
print (adjacentDups(myList1)) #False

myList2 = [1,2,3,4,4,5,6,7,8,9]
print (myList2)
print (adjacentDups(myList2)) #True

## Output
## [2, 4, 3, 6, 8, 5, 9, 7, 5, 7]
## False
## [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
## True


