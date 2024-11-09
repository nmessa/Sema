##HiLo Game Version 3
##Author: nmessa
##Date: 11/6/2024

from random import randint

secret = randint(1, 100)
guessed = False
count = 0
while not guessed:
    guess = int(input("Guess a number form 1 to 100: "))
    count += 1
    if guess == secret:
        print("You guessed the number in", count, "guesses")
        guessed = True
    elif guess > secret:
        print("You guessed high")
    else:
        print("You guessed low")

##Sample Output
##Guess a number form 1 to 100: 50
##You guessed low
##Guess a number form 1 to 100: 75
##You guessed low
##Guess a number form 1 to 100: 87
##You guessed high
##Guess a number form 1 to 100: 80
##You guessed low
##Guess a number form 1 to 100: 83
##You guessed high
##Guess a number form 1 to 100: 82
##You guessed the number in 6 guesses
