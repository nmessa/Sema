## Lab Exercise 11/1/2023 Problem 1
## Author: nmessa
## Filename: dna1.py
## This program demonstrates DNA sequence matching

#create test sequence
strand = "AACAACTTCGTAAGTAA"
look = "TCGT"

#search sequence
location = strand.find(look)
if location == -1:
    print ("Sequence not found")
else:
    print ("Sequence found at location", location)

##Output
##Sequence found at location 7

