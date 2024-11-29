## Lab Exercise 10/13/2023 Problem 2
## Author: nmessa
## Silly sentence generator writing them to a file
## Files are stored in a text file with one element per line

from random import *

#open files and read to lists
#open adjectives.txt and read files to the list adjectives
myFile = open('adjectives.txt', 'r')
adjectives = myFile.readlines()
myFile.close()
#strip off newline characters
for i in range(len(adjectives)):
    adjectives[i] = adjectives[i].rstrip()
     
#open nouns.txt and read files to the list nouns
myFile = open('nouns.txt', 'r')
nouns = myFile.readlines()
myFile.close()
for i in range(len(nouns)):
    nouns[i] = nouns[i].rstrip()

#open adverbPhrases.txt and read files to the list adverbPhrses
myFile = open('adverbPhrases.txt', 'r')
adverbPhrases = myFile.readlines()
myFile.close()
#strip off newline characters
for i in range(len(adverbPhrases)):
    adverbPhrases[i] = adverbPhrases[i].rstrip()

#open verbPhrases.txt and read files to the list verbPhrses
myFile = open('verbPhrases.txt', 'r')
verbPhrases = myFile.readlines()
myFile.close()
#strip off newline characters
for i in range(len(verbPhrases)):
    verbPhrases[i] = verbPhrases[i].rstrip()

#Create the sentence
sentence = 'The ' + choice(adjectives) + " " + choice(nouns) + " " + \
           choice(verbPhrases) + " " + choice(adverbPhrases) + '\n'

#Print the sentence
print (sentence)



