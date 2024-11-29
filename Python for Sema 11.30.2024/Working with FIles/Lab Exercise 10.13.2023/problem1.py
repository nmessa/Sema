## Lab Exercise 10/13/2023 Problem 1
## Author: nmessa
## Write info to a file

name = input("Enter a name: ")
age = input("Enter age: ")
color = input("Enter favorite color: ")
food = input("Enter favorite food: ")

outfile = open("info.txt", 'w')
outfile.write(name + '\n')
outfile.write(age + '\n')
outfile.write(color + '\n')
outfile.write(food + '\n')
outfile.close()
