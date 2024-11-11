## Lab Exercise 10/8/2024 Problem 3a
## Author: nmessa
## This program creates a list of unique numbers
from random import *

numbers = set()

while len(numbers) <= 10:
    num = randint(1, 100)
    numbers.add(num)

print (numbers)
