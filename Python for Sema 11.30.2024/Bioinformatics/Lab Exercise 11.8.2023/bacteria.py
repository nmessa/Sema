#bacteria.py
#Author: nmessa
#Date: 11.3.2023
import math

#Get user input
n = int(input("Enter the initial bacteria count: "))
k = float(input("Enter contant amount: "))
t = float(input("Enter the growth time period in hours: "))


#Calculate final bacteria count
y = n * math.exp(k * t)

#Output results
print(int(y), "bacteria will be present after", t, "hours")

##Output
##Enter the initial bacteria count: 5
##Enter contant amount: .8
##Enter the growth time period in hours: 8
##3009 bacteria will be present after 8.0 hours
