## Lab Exercise 10/8/2024 Problem 3
## Author: nmessa
## This program creates a list of unique numbers
from random import *

numbers = []

while len(numbers) <= 10:
    num = randint(1, 100)
    if num not in numbers:
        numbers.append(num)

print (numbers)
