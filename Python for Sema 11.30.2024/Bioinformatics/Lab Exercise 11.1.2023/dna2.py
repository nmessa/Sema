## Lab Exercise 11/1/2023 Problem 2
## Author: nmessa
## Filename: dna2.py
## This program demonstrates DNA sequence matching

import random
BASES = ['G', 'A', 'T', 'C']
strand = ""

#generate a DNA string of one million bases
for i in range(1000000):
    strand += random.choice(BASES)

#Enter DNA sequence to search for
look = input("Enter the DNA sequence to search for (G, A, T, C): ").upper()

#search sequence
location = strand.find(look)
if location == -1:
    print ("Sequence not found")
else:
    print ("Sequence found at location", location)

##Sample Output
##Enter the DNA sequence to search for (G, A, T, C): ACTGCTAG
##Sequence found at location 11850

