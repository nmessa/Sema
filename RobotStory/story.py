#story.py
#Author: nmessa
#Date: 10/31/2023

letters = ['01110100', '01101001', '01101110', '01111001',
           '00100000', '01110011', '01110100', '01101111',
           '01110010', '01101001', '01100101', '01110011']

story = ""

for letter in letters: #Go through each 'letter'
    story += chr(int(letter, 2))#convert letter to integer
                                #specify base 2 number system
                                #then turn into a character
                                #and add character to story
print(story)
