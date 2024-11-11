#Magic 8 Ball
#Author: nmessa
#Date: 1.29.2024

from random import randint, choice
from time import sleep

replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]

answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]

again = True
while again:
    #Give introductory message
    print ("Welcome to the all knowing Magic Eight Ball")
    sleep(0.5)
    print ("Ask me any yes/no question")

    #Get question from user
    input("> ")

    #Let Magic 8 Ball think for a while
    pause = randint(3, 8)
    for i in range (pause):
        print(". ", end = "")
        sleep(0.7)
    print()

    #Let Magic 8 Ball generate a reply
    print (choice(replies))
    sleep(5)

    #Let Magic 8 Ball generate an answer
    print("I have an answer!")
    sleep(1)
    print(choice(answers))

    print("Do you wish to ask another question (y/n)")
    answer = input(">")
    if answer == 'n':
        again = False

