##HiLo Game Version 1
##Author: nmessa
##Date: 11.6.2023

from random import randint

secret = randint(1, 10)
guess = int(input("Guess a number form 1 to 10: "))
if guess == secret:
    print("You guessed the number")
elif guess > secret:
    print("You guessed high")
else:
    print("You guessed low")

##Sample Output
##Guess a number form 1 to 10: 5
##You guessed high
