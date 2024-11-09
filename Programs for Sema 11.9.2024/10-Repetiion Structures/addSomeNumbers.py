#addSomeNumbers.py
#Author: nmessa
#Date: 11.6.2023

total = 0
count = 0
number = int(input("enter an integer (enter 0 to quit): "))
while number != 0:
    count += 1
    total += number
    number = int(input("enter an integer (enter 0 to quit): "))
    
average = total/count
print("You entered", count, "numbers that totaled", total, "and averaged",average)  
    
##Sample Output
##enter an integer (enter 0 to quit): 43
##enter an integer (enter 0 to quit): 76
##enter an integer (enter 0 to quit): 34
##enter an integer (enter 0 to quit): 98
##enter an integer (enter 0 to quit): 0
##You entered 4 numbers that totaled 251 and averaged 62.75
