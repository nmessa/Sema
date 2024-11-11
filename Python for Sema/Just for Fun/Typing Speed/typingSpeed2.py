#Lab Exercise 12.5.2017 Problem 3
#Author: nmessa
#This program calculates typing speed and accuracy

from time import *
from random import *

#Calculate the accuracy of the typed text versus test text
def calcAccuracy(st, txt):
    count = 0

    #split typed text and test text into individual words
    st = st.split()
    txt = txt.split()

    #check each word for correctness and keep count of the errors
    for i in range(len(txt)):
        if st[i] != txt[i]:
            count += 1
    return count/len(txt) * 100  #return the percentage of errors
    
#Calculates how many word in your typed text
def howManyWords(phrase):
    numWords = 0
    for ch in phrase:
        if ch == ' ':
            numWords += 1
    return numWords + 1

#Inialize test text and typed text
s = ''
text = ''

#Typing test phrases
phrases = ['Now is the time for all good men to come to the aid of their country',
           'The quick brown fox jumps over the lazy dog',
           'Jack be nimble Jack be quick Jack jumped over the candlestick',
           'We promptly judged antique ivory buckles for the next prize',
           'How razorback jumping frogs can level six piqued gymnasts',
           'Sixty zippers were quickly picked from the woven jute bag',
           'Crazy Fredrick bought many very exquisite opal jewels']

print("When you see a phrase, type it in and hit enter")

#Provide countdown
for i in range(5, 0, -1):
    print(i)
    sleep(1)
print("Go!!!!")

start_time = time() #Start the clock

#Type 3 random phrases
for i in range(3):
    phrase = choice(phrases)
    text += phrase + ' '
    print(phrase)
    s += input()
    s += ' '

end_time = time()  #Stop the clock

#Calculate words per minute
wps = howManyWords(s)/(end_time - start_time)
wpm = wps * 60

#report result
print("You are typing at", wpm, 'words per minute')

#Calculate the error rate
errorRate = calcAccuracy(s, text)

#report result
print("The error rate is", errorRate, '%')

