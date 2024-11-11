# 
# Word Guess game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess =''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guess += secretWord[i]
        else:
            guess += '_ '
    return guess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = 'abcdefghijklmnopqrstuvwxyz'
    avail = ''
    for i in range(len(letters)):
        if letters[i] not in lettersGuessed:
            avail += letters[i]
    return avail

def wordGuess(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Word Guess.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    mistakesMade = 0
    guessesLeft = 8
    wordGuessed = False
    guessedWord = getGuessedWord(secretWord, lettersGuessed)
    print("Welcome to the game Word Guess!")
    print("I am thinking of a word that is " + str(len(secretWord)) +
          " letters long")
    
    while guessesLeft > 0 and not wordGuessed:
        print("---------------------")
        print("You have " + str(guessesLeft) + " guesses left")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters: " + availableLetters)
        guess = input("Please guess a letter: ")
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter" + guessedWord)
        else:
            lettersGuessed.append(guess)
            if guessedWord != getGuessedWord(secretWord, lettersGuessed):
                guessedWord = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess: " + guessedWord)
                if isWordGuessed(secretWord, lettersGuessed):
                    wordGuessed = True
            else:
                print("Oops! That letter is not in my word: " + guessedWord)
                mistakesMade += 1
                guessesLeft -= 1
    print("---------------------")           
    if guessesLeft > 0:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses.  The word was " + secretWord)

# When you've completed your wordGuess function, uncomment these two lines and run this file to test!

secretWord = chooseWord(wordlist).lower()
wordGuess(secretWord)
