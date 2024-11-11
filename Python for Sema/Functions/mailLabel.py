##mailLabel.py
##Author: nmessa
##Date: 12.4.2023
##This program allows the user to enter their address info and prints
##a mailing label

def mailingLabel(n, a, c, s, z):
    print(n)
    print(a)
    print(c +", " + s + "   ", z)

name = input("Enter your name: ")
address = input("Enter your address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zipcode = input("Enter your zipcode: ")
mailingLabel(name, address, city, state, zipcode)

##Output
##Enter your name: Herman Munster
##Enter your address: 13 Mockingbird Lane
##Enter your city: Exeter
##Enter your state: NH
##Enter your zipcode: 03909
##Herman Munster
##13 Mockingbird Lane
##Exeter, NH    03909
