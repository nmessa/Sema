#printBackards.py
#Author: nmessa
#Date: 11.6.2023

sentence = input("Enter a sentence: ")
for i in range(len(sentence)-1, -1, -1):
    print(sentence[i], end = "")

print() #print a blank line

#alternate method using "string slicing"
print(sentence[::-1])
