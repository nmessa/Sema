#playAgain.py
#Author: nmessa
#Date: 11.6.2023

quit = False

while not quit:
    choice = input("Play again (y/n): ")
    if choice != 'y':
        quit = True
print("Bye Bye!!!")

##Sample Output
##Play again (y/n): y
##Play again (y/n): y
##Play again (y/n): y
##Play again (y/n): n
##Bye Bye!!!
