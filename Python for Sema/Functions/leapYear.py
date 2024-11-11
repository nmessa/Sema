## Lab Exercise 10/7/2024 Problem 2
## Author: nmessa
## Writes a function to determine if a year is a leap year

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

#Test code
print (isLeapYear(1996))  #True
print (isLeapYear(1900))  #False
print (isLeapYear(2000))  #True
print (isLeapYear(1993))  #False
