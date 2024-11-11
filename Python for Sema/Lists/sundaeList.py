## Lab Exercise 10/9/2024 Problem 3
## Author: nmessa
## This program generates all permutations of the 5 flavors of ice cream
## choosing 3 at a time

from random import *

#Create an empty list to hold permutations
permutationList = []

#Create a list to hold 5 flavors of ice cream
flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Cherry', 'Peach']

#Create an empty list to hold the sundaes
sundae = []

count = 0 #keep track to the number of sundaes in the permutation list
count2 = 0 #keep track of the number of flavors added to sundae


while count < 60:
    #generate a sundae
    while count2 < 3:
        temp = choice(flavors)
        if temp not in sundae:
            sundae.append(temp)
            count2 += 1
    #reset count2 to generate the next sundae
    count2 = 0

    #Add sundae to permutationList if not already in list and add 1 to count
    if sundae not in permutationList:
        permutationList.append(sundae)
        count += 1
    #reset the sundae list for the next sundae
    sundae = []

#Print the sundaes
for i in range(len(permutationList)):
    print(permutationList[i])
    
#print(sundae) #for testing purposes

##Output
##['Chocolate', 'Strawberry', 'Peach']
##['Chocolate', 'Peach', 'Cherry']
##['Strawberry', 'Chocolate', 'Peach']
##['Strawberry', 'Vanilla', 'Cherry']
##['Cherry', 'Peach', 'Strawberry']
##['Strawberry', 'Chocolate', 'Cherry']
##['Strawberry', 'Cherry', 'Peach']
##['Cherry', 'Vanilla', 'Chocolate']
##['Peach', 'Cherry', 'Chocolate']
##['Cherry', 'Vanilla', 'Strawberry']
##['Strawberry', 'Vanilla', 'Chocolate']
##['Cherry', 'Strawberry', 'Vanilla']
##['Vanilla', 'Strawberry', 'Peach']
##['Peach', 'Strawberry', 'Cherry']
##['Chocolate', 'Strawberry', 'Cherry']
##['Vanilla', 'Cherry', 'Strawberry']
##['Cherry', 'Strawberry', 'Peach']
##['Strawberry', 'Peach', 'Chocolate']
##['Vanilla', 'Chocolate', 'Strawberry']
##['Chocolate', 'Vanilla', 'Strawberry']
##['Peach', 'Chocolate', 'Strawberry']
##['Cherry', 'Chocolate', 'Vanilla']
##['Vanilla', 'Peach', 'Strawberry']
##['Vanilla', 'Cherry', 'Chocolate']
##['Chocolate', 'Strawberry', 'Vanilla']
##['Vanilla', 'Peach', 'Chocolate']
##['Chocolate', 'Peach', 'Vanilla']
##['Vanilla', 'Strawberry', 'Cherry']
##['Cherry', 'Strawberry', 'Chocolate']
##['Cherry', 'Vanilla', 'Peach']
##['Strawberry', 'Cherry', 'Vanilla']
##['Peach', 'Vanilla', 'Cherry']
##['Vanilla', 'Peach', 'Cherry']
##['Peach', 'Cherry', 'Vanilla']
##['Cherry', 'Peach', 'Chocolate']
##['Strawberry', 'Peach', 'Cherry']
##['Vanilla', 'Chocolate', 'Peach']
##['Vanilla', 'Cherry', 'Peach']
##['Peach', 'Vanilla', 'Chocolate']
##['Vanilla', 'Strawberry', 'Chocolate']
##['Peach', 'Strawberry', 'Chocolate']
##['Cherry', 'Chocolate', 'Strawberry']
##['Chocolate', 'Cherry', 'Strawberry']
##['Peach', 'Cherry', 'Strawberry']
##['Peach', 'Chocolate', 'Cherry']
##['Peach', 'Strawberry', 'Vanilla']
##['Strawberry', 'Vanilla', 'Peach']
##['Chocolate', 'Vanilla', 'Peach']
##['Chocolate', 'Cherry', 'Peach']
##['Chocolate', 'Cherry', 'Vanilla']
##['Peach', 'Chocolate', 'Vanilla']
##['Strawberry', 'Chocolate', 'Vanilla']
##['Vanilla', 'Chocolate', 'Cherry']
##['Cherry', 'Chocolate', 'Peach']
##['Cherry', 'Peach', 'Vanilla']
##['Peach', 'Vanilla', 'Strawberry']
##['Strawberry', 'Peach', 'Vanilla']
##['Strawberry', 'Cherry', 'Chocolate']
##['Chocolate', 'Vanilla', 'Cherry']
##['Chocolate', 'Peach', 'Strawberry']

