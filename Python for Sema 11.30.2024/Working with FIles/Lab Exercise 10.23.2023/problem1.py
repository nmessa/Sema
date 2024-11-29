#Lab Exercise 10.23.2023 Problem 1
#Author: nmessa
#This program will read lines from forward.txt and write them back to
#a file backwards.txt

def reverseWord(w):
    return w[::-1]

#Open file to read
inFile = open("forward.txt", "r")

#read all lines and store in list lines
lines = inFile.readlines()

#close the file
inFile.close()

#open a file to write
outFile = open("backwards.txt", "w")

#process each line from the file
for line in lines:
    words = line.split()
    #Process each word in the line
    for word in words:
        temp = reverseWord(word)
        outFile.write(temp + " ")
    outFile.write('\n')
        
#close the file
outFile.close()

## forward.txt
## This is a test
## of reading files
## Jack be nimble
## Jack be quick
## Mary had a little lamb
## Whose fleece looked like a candlestick
## It was not fireproof
##
## backwards.txt       
## sihT si a tset 
## fo gnidaer selif 
## kcaJ eb elbmin 
## kcaJ eb kciuq 
## yraM dah a elttil bmal 
## esohW eceelf dekool ekil a kcitseldnac 
## tI saw ton foorperif
