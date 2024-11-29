## Lab Exercise 10/12/2023 Problem 1 and 2
## Author: nmessa
## This program will write a name and address to a file

#Get input from user
name = input("Enter your name: " )
address = input("Enter your street address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zip = input("Enter your ZIP code: ")
csz = city + ', ' + state + '   ' + zip

#write user input to a file
myFile = open('label.txt', 'w')
myFile.write(name + '\n')
myFile.write(address + '\n')
myFile.write(csz)
myFile.close()

#read from a file and read in text
myFile = open('label.txt', 'r')
lines = myFile.readlines()
myFile.close()

#display the text
for line in lines:
    print (line,end = '')
    
##Sample Output
##Enter your name: Joe Smith
##Enter your street address: 12 Main Street
##Enter your city: Exeter
##Enter your state: NH
##Enter your ZIP code: 03833
##Joe Smith
##12 Main Street
##Exeter, NH   03833

