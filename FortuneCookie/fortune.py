from random import randint

#This function returns a random fortune number based
#on ASCII values of the characters in your name
def nameVal(s):
    total = 0
    for ch in s:
        total += ord(ch)
    return total % randint(0, len(cookie)-1)

#Open phrases.text file for reading
myFile = open("phrases.txt", "r")

#Create an empty list to hold fortunes
cookie = []

#Read all fortunes from file and add to list
phrases = myFile.readlines();
for line in phrases:
    cookie.append(line.rstrip())

#Close the phrases.txt file
myFile.close()

#Enter your name and print your fortune
name = input("Enter your name: ")
print(cookie[nameVal(name)])

lucky = []
while len(lucky) < 5:
    temp = randint(1, 99)
    if temp not in lucky:
        lucky.append(temp)
lucky.sort()
print("Lucky numbers: ", end = " ")
for i in lucky:
    print(i, end = " ")
print()
    
