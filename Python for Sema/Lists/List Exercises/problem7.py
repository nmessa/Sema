## Lab Exercise 10/22/2024 Problem 7
## Author: nmessa
## return the second largest element in the list

def returnSecondLargest(lst):
    largest = max(lst)
    while largest in lst:
        lst.remove(largest)
    return max(lst)
    
#Code to test the function
myList = [2,4,3,6,8,5,9,9,5,7]
print (myList)
print (returnSecondLargest(myList)) #8

## Output
## [2, 4, 3, 6, 8, 5, 9, 9, 5, 7]
## 8


