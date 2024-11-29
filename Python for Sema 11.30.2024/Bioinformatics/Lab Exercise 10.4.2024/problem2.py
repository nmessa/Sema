## Lab Exercise 10.4.2024 Problem 2
## Author: nmessa
## This program uses a function to return the reverse complement of a DNA string
def reverseComplement(dna):
    #base conversion dictionary
    baseConvert = {'G':'C', 'C':'G', 'A':'T', 'T':'A', 'N':'N'}

    #Declare variables reverse and complement as null strings
    reverse = ""
    complement = ""
    
    #reverse the DNA strand
    for i in range(len(dna)-1, -1, -1):
        reverse += dna[i]
    #print(reverse)

    #Complement the DNA strand
    for base in reverse:
        complement += baseConvert[base]
    return complement

#Test code
print(reverseComplement('ACGTAAGTCA'))

