## Lab Exercise 12/19/2023 Problem 3
## Author: nmessa
## This program will sort a list of words from shortest to longest

words = "Now is the time for all good men to come to the aid" + \
        " of their country"
words = words.split()

stuff = [[len(w), w] for w in words]
stuff.sort()

for i in stuff:
    print (i[1], "    ", i[0])

##Output
##is      2
##of      2
##to      2
##to      2
##Now      3
##aid      3
##all      3
##for      3
##men      3
##the      3
##the      3
##come      4
##good      4
##time      4
##their      5
##country      7
