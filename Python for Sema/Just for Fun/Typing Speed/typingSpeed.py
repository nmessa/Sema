#Lab Exercise 12/5/2017 Problem 2
#Author: nmessa
#This program will measure the typing speed of the user

from time import *

def howManyWords(phrase):
    numWords = 0
    for ch in phrase:
        if ch == ' ':
            numWords += 1
    return numWords + 1
    
s = ""

#Provide countdown
print("Start typing until you have typed 100 characters:")
for i in range(5, 0, -1):
    print(i)
    sleep(1)
print("Go!!!!")

start_time = time() #Start the clock

#Type words until you have 100 characters
while len(s) < 100:
    s += input()
    s += ' '

end_time = time()  #Stop the clock

#Calculate words per minute
wps = howManyWords(s)/(end_time - start_time)
wpm = wps * 60

#Print report
print("You are typing at", round(wpm, 2), 'words per minute')
