#Demonstration of the use of print function to output
#Author: nmessa
#Date: 10.30.2023

str1 = "Hello"
str2 = "World"
str3 = "The best number is"
number = 42

#2 ways to print "Hello World"
print(str1, str2)
print(str1 + " " + str2)

#print "Hello World"
print(str1, end = " ")       #the end = " " parameter supresses the newline
print(str2)

#2 ways to print "The best number is 42"
print(str3, number)
print(str3 + " " + str(number))

##Output
##Hello World
##Hello World
##Hello World
##The best number is 42
##The best number is 42
