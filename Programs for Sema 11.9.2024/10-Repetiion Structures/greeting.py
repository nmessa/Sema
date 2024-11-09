##greeting.py
##Author: nmessa
##Date: 11.7.2024

keepGoing = True

while keepGoing:
    print("Hello")
    answer = input("Greet again (y/n): ")
    if answer == 'n':
        print("Good Bye")
        keepGoing = False

##Sample Output
##Hello
##Greet again (y/n): y
##Hello
##Greet again (y/n): y
##Hello
##Greet again (y/n): n
##Good Bye
