##Lab Exercise 12.22.2022 Problem 2
##Author: nmessa
##This program displays all of the worlds' countries and the user will enter
##one of the countries and the program will display the capital.

#This function returns the name of the capital of a given country
def findCapital(country):
    for i in range(len(countries)):
        if countries[i] == country:
            return capitals[i]
    return "Country not found"


#This function prints the countries in the database   
def printCountries():
    print("Countries in database")
    print (countries[0] , end = '   ')
    for i in range(1, len(countries)):
        if (i%4 != 0):
            print (countries[i] , end = '   ')
        else:
            print (countries[i] , end = '\n')
    print()

##Read in data from text file
file = open('capitals.txt', 'r')
lines = file.readlines()
print(str(len(lines)) + ' capitals loaded')

##Create country and captitals list
countries = []
capitals = []

##Process each country and capital data
for line in lines:
    cap = line.split(' - ')
    countries.append(cap[0])
    capitals.append(cap[1])

##Print the countries as a convience to the user
printCountries()

##Process the query
again = True
while again:
    country = input("Enter the name of the country: ")
    print ("Capital of", country, "is", findCapital(country))
    repeat = input("Another country? (y/n)")
    if repeat == 'n':
        again = False
    else:
        printCountries()
        
print("Thank you for using Capital Finder Pro")
