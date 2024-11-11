##ageSeconds.py
##Author: nmessa
##Date: 12.5.2023
##This program will calculate your age in seconds

def ageInSeconds(years):
    myAge = years * 365 * 24 * 60 * 60
    return myAge

age = int(input("Enter your age: "))
ageSeconds = ageInSeconds(age)
print("Your age in seconds =", ageSeconds)

##Sample Output
##Enter your age: 12
##Your age in seconds = 378432000
