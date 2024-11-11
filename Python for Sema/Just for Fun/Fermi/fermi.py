## Game of Fermi Version 1.0
## Author: nmessa
## Date: 1/8/2018
## The goal of the game is for the player to guess the digits in
## the three positions in the least number of tries.  For each guess,
## the player provides three digits for position 1, 2, and 3.
## The program replies with a hint consisting of Fermi, Pico, and Nano.
## If the digit guess for a given position is correct, then the reply is Fermi.
## If the digit guessed for a given position is in a different position, then
## the reply is Pico.  If the digit guessed for a given position does not match
## any of the three digits, then the reply is Nano.  

from random import *

#Create two lists
numbers = [1,2,3,4,5,6,7,8,9]
secret = []  #secret code

#Build the secret number of 3 unique numbers from 1 to 9
while len(secret) < 3:
    temp = choice(numbers)
    if temp not in secret:
        secret.append(temp)

#Set boolean flag variable
win = False

numGuesses = 0  #keep track of numbers guessed

#Play a round
while not win:
    #initialize counter and phrase list
    count = 0
    phrases = []  #This will hold the output phrase such as Fermi Nano Pico

    #Get number guess from user
    temp = input("Enter 3 numbers (1 - 9) separated by spaces: ").split()

    #Build a list that represents the number guessed
    guess = [int(temp[0]), int(temp[1]), int(temp[2])]

    #update number of guesses
    numGuesses += 1

    #Algorithm to test number and generate 3 phrases
    for n in guess:
        if n in secret:
            if n == secret[count]:
                phrases.append('Fermi')
            else:
                phrases.append('Pico')
        else:
            phrases.append('Nano')
        count += 1

    #Print the result of algorithm execution
    for p in phrases:
        print(p, end = ' ')
    print()
    
    if phrases.count('Fermi') == 3:  #this means you won
        print('You won in', numGuesses, 'guesses')
        win = True

if numGuesses < 5:
    print("You are a genius")
elif numGuesses < 9:
    print("You have an organized brain")
else:
    print("Your mind is too chaotic")
    
## Sample Output
## Enter 3 numbers (1 - 9)seperated by spaces:  6 3 5
## Nano Pico Nano 
## Enter 3 numbers (1 - 9)seperated by spaces:  3 4 2
## Pico Pico Nano 
## Enter 3 numbers (1 - 9)seperated by spaces:  4 3 7
## Fermi Pico Nano 
## Enter 3 numbers (1 - 9)seperated by spaces:  4 8 3
## Fermi Fermi Fermi 
## You won in 4 guesses
## You are a genius

