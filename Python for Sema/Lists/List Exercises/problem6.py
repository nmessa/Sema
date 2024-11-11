## Lab Exercise 10/22/2024 Problem 6
## Author: nmessa
## Move even element of a list to the front

def moveEvenToFront(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            temp = lst[i]
            for j in range(i, 0, -1):
                lst[j] = lst[j-1]
            lst[0] = temp
    return lst
    
        

#Code to test the function
myList = [1,2,3,4,5,6,7,8,9,10]
print (myList)
print (moveEvenToFront(myList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]


