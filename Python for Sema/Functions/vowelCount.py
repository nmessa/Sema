##vowelCount.py
##Author: nmessa
##Date: 12.4.2023
##This program uses a function to count all vowels

def countVowels(s):
    vowels = "AIEOUaeiou"
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count

phrase = input("Enter a phrase: ")
result = countVowels(phrase)
print(phrase, "contains", result, "vowels")

##Output
##Enter a phrase: This is a test
##This is a test contains 4 vowels
