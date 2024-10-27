##Lab Exercise 1.19.2024 Problem 1
##Author: nmessa

def inatorInator(s):
    length = len(s)
    consonants = "bcdfghjklmnpqrstvwxyz"
    if s[-1] in consonants:
        return s + "inator " + str(length) + "000"
    else:
        return s + "-inator " + str(length) + "000"

print(inatorInator("Shrink"))
print(inatorInator("Doom"))
print(inatorInator("EvilClone"))

##Output
##Shrinkinator 6000
##Doominator 4000
##EvilClone-inator 9000
