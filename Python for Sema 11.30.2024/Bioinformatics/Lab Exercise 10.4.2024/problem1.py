## Lab Exercise 10.4.2024 Problem 1
## Author: nmessa
## This program generates a DNA string and reports the percentage of
## GC content
from random import choice
#Define bases
bases = ['G', 'C', 'A', 'T', 'N']

#initialize DNA string
dna = ""
count = 0
NUM_BASES = 1000000

#build a million base DNA string
for i in range(NUM_BASES):
    dna += choice(bases)

#count the G and C bases
for base in dna:
    if base == 'G' or base == 'C':
        count += 1
#Calculate the percentage of C and G bases in the DNA strand
percent = count/NUM_BASES * 100
print("The percentage of GC material is", round(percent, 2))

