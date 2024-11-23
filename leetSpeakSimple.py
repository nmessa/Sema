##leetSpeakSimple.py
##Author: nmessa
##Date: 11/22/2024

translate = {'A':'4','E':'3', 'G':'6', 'O':'0', 'S':'5', 'T':'7', 'Z':'2'}

phrase = input("Enter a phrase: ").upper()

for letter in phrase:
    if letter in translate.keys():
        print(translate[letter], end = "")
    else:
        print(letter, end = "")
    
##Sample Output
##Enter a phrase: I am teaching Python to Sema
##I 4M 734CHIN6 PY7H0N 70 53M4
