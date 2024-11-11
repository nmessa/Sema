##vowelCensor.py
##Author: nmessa
##Date: 12.4.2023
##This program uses a function to replace all vowels with a "*"

def censorVowels(s):
    vowels = "AIEOUaeiou"
    sNew = ""
    for letter in s:
        if letter in vowels:
            sNew += "*"
        else:
            sNew += letter
    return sNew

phrase = input("Enter a phrase: ")
result = censorVowels(phrase)
print(phrase, "is now", result)


##Output
##Enter a phrase: This is a test
##This is a test is now Th*s *s * t*st
        
