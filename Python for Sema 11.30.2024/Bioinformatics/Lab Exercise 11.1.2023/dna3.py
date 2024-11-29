## Lab Exercise 11/1/2023 Problem 3
## Author: nmessa
## Filename: dna3.py
## This program demonstrates DNA sequence matching with user validation

import random
BASES = ['G', 'A', 'T', 'C']
strand = ""

def validateSequence(sequence):
    for base in sequence:
        if base not in BASES:
            return False
    return True

#generate a DNA string of one million bases
for i in range(1000000):
    strand += random.choice(BASES)

#Enter DNA sequence to search for
look = input("Enter the DNA sequence to search for (G, A, T, C): ").upper()

if validateSequence(look):
    #search sequence
    location = strand.find(look)
    if location == -1:
        print ("Sequence not found")
    else:
        print ("Sequence found at location ", location)
else:
    #print invalid sequence message
    print ("Invalid sequence to search for entered")

##Sample Output
##Enter the DNA sequence to search for (G, A, T, C): GCTADGC
##Invalid sequence to search for entered
