##Lab Exercise 12.22.2022 Problem 2a
##Author: nmessa
##This program displays all of the worlds' countries in a menu and the user will enter
##one of the countries numbers and the program will display the capital.

#This function returns the name of the capital of a given country
def findCapital(country):
    for i in range(len(countries)):
        if countries[i] == country:
            return capitals[i]
    return "Country not found"


#This function prints the countries in the database   
def printCountries():
    print("Contries in database")
    for i in range(0, len(countries)):
        print(i+1, countries[i])
    print()
    number = int(input("Enter the country number: "))
    return number
                 

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

#Create dictionary of countries
countryDict = {}
for i in range(0, len(countries)):
    countryDict[i+1] = countries[i]   
    

##Process the query
again = True
while again:
    countryNumber = printCountries()
    country = countryDict[countryNumber]
    print ("Capital of", country, "is", findCapital(country))
    repeat = input("Another country? (y/n)")
    if repeat == 'n':
        again = False
        
print("Thank you for using Capital Finder Pro")
