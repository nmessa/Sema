## Lab Exercise 10/12/2023 Problem 4 and 5
## Author: nmessa
## This program will translate an English phrase to Pig Latin and write
## it to a file.  It will also read a Pig Latin file and display it
## in English
## Modified to be case insensitive

vowels = 'aeiouh'

def toPig(word):
    if word[0] in vowels:
        return word + 'hay'
    else:
        return word[1:] + word[0] + 'ay'

def toEnglish(word):
    #add code to translate Pig Latin to English
    if word[-3:] == 'hay':
        return word[0:-3]
    else:
        return word[-3] + word[0:-3]

phrase = input("Enter a phrase: ").lower()
words = phrase.split()

#Write Pig Latin file
myFile = open('pigLatin.txt', 'w')
for word in words:
    myFile.write(toPig(word) + ' ')

myFile.close()

#Read and translate Pig Latin file
myFile = open('pigLatin.txt', 'r')
myFile2 = open('english.txt', 'w')
words = myFile.readline().split()
myFile.close()

for word in words:
    print (word, end = ' ')
print()
for word in words:
    print (toEnglish(word), end = ' ')
    myFile2.write(toEnglish(word) + ' ')
myFile2.close()

    

