## Lab Exercise 10.4.2024 Problem 3
## Author: nmessa
## This program has a function that tests for Stop Codons given a DNA string
## and a reading frame

#This function given a DNA strand and frame number will determine whether
#or not a stop codon exists
#Stop codons are TAA, TAG, and TGA
#Use string slicing
def hasStopCodon(dna, frame):
    for i in range(frame, len(dna), 3):
        if dna[i:i+3] == 'TAA' or dna[i:i+3] == 'TAG' or dna[i:i+3] == 'TGA':
            return True
    return False

#Test code
dna = 'TAAGCCGAT'
print(hasStopCodon(dna, 0)) #True
dna = 'TAAGCCGAT'
print(hasStopCodon(dna, 1)) #False
dna = 'TATAGCGAT'
print(hasStopCodon(dna, 2)) #True
dna = 'TTGACCGAT'
print(hasStopCodon(dna, 1)) #True
dna = 'TCGGCTAGT'
print(hasStopCodon(dna, 2)) #True
dna = 'TATAGCGAT'
print(hasStopCodon(dna, 1)) #False


