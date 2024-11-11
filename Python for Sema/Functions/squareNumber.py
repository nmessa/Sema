##squareNumber.py
##Author: nmessa
##Date: 12.4.2023
##This program uses a function to calculate the square of a number

def squareNumber(n):
    return n * n

number = float(input("Enter a number: "))
answer = squareNumber(number)
print(str(number) + " squared = " + str(answer))

##Output
##Enter a number: 25
##25.0 squared = 625.0
