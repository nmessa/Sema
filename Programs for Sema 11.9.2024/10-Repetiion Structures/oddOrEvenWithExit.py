##identify odd and even numbers with an exit
##Author: nmessa
##Date: 11.7.2024

while True:
    number = int(input("Enter a number (0 to quit): "))
    if number == 0:
        print("Bye-Bye")
        break
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")
        
##Sample Output
##Enter a number (0 to quit): 56
##Even
##Enter a number (0 to quit): 44
##Even
##Enter a number (0 to quit): 31
##Odd
##Enter a number (0 to quit): 67
##Odd
##Enter a number (0 to quit): 0
##Bye-Bye
