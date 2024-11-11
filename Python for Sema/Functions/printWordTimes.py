##printWordTimes.py
##Author: nmessa
##Date: 12.4.2023
##This prints a word a specified number of times

def printWordTimes(w, n):
    for i in range(n):
        print(w)

word = input("Enter a word: ")
times = int(input("How many times to print the word: "))
printWordTimes(word, times)

##Output
##Enter a word: happy
##How many times to print the word: 5
##happy
##happy
##happy
##happy
##happy
