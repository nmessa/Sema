## Lab Exercise 10/8/2024 Problem 4
## Author: nmessa
## This program filters a list
numbers = []

# Function receives a list and which multiple to remove
# during the execution of the function the list will shrink
# as elements are removed
##def removeMults(nums, mult):
##    i = 0
##    while i < len(nums):
##        if nums[i]%mult == 0:
##            nums.remove(nums[i])
##        i += 1
##    return nums

#Alternate solution
def removeMults(nums, mult):
    for number in nums:
        if number%mult == 0:
            nums.remove(number)
    return nums

#initialize list        
for i in range(2, 1001):
    numbers.append(i)

#remove all multiples
for i in range(2, 101):
    removeMults(numbers, i)

#put the 2 to 100 back into the list
for i in range(2, 101):
    numbers.append(i)
    
numbers.sort()
print (numbers)

