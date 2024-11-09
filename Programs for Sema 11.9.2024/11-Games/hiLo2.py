##HiLo Game Version 2
##Author: nmessa
##Date: 11/6/2024

from random import randint

secret = randint(1, 100)
guessed = False
while not guessed:
    guess = int(input("Guess a number form 1 to 100: "))
    if guess == secret:
        print("You guessed the number")
        guessed = True
    elif guess > secret:
        print("You guessed high")
    else:
        print("You guessed low")

##Sample Output
##Guess a number form 1 to 100: 50
##You guessed low
##Guess a number form 1 to 100: 75
##You guessed high
##Guess a number form 1 to 100: 67
##You guessed high
##Guess a number form 1 to 100: 62
##You guessed the number
