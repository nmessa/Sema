##Lab Exercise 11/9/2023 Problem 8
##Author: nmessa
##Program generated the complimentary DNA strand

import random
BASES = ['C', 'G', 'A', 'T']
translate = {'C':'G', 'G':'C', 'A':'T', 'T':'A'}
SIZE = 100

strand = ""
complement = ""

#Create original strand
for i in range(SIZE):
    strand += random.choice(BASES)

#Build complement
for i in strand:
    complement += translate[i]

print (strand)
print (complement)
    
