#Lab Exercise 10.23.2023 Problem 2
#Author: nmessa
#This program will read lines from regular.txt filter out the short words
#and write back words greater than 2 characters to a file shorter.txt

#Open file to read
inFile = open("regular.txt", "r")

#read all lines and store in list lines
lines = inFile.readlines()

#close the file
inFile.close()

#open a file to write
outFile = open("shorter.txt", "w")

#process each line from the file
for line in lines:
    words = line.split()
    #Process each word in the line
    for word in words:
        #if word is greater than 2 characters write to file
        if len(word) >= 3:
            outFile.write(word + " ")
    #goo to next line
    outFile.write('\n')
        
#close the file
outFile.close()

## regular.txt
## This is a test
## of reading files
## Jack be nimble
## Jack be quick
## Mary had a little lamb
## Whose fleece looked like a candlestick
## It was not fireproof
##
## shorter.txt       
## This test 
## reading files 
## Jack nimble 
## Jack quick 
## Mary had little lamb 
## Whose fleece looked like candlestick 
## was not fireproof
