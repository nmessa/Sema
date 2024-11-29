## Lab Exercise 11/9/2023 Problem 7
## Author: nmessa
## Program to determine the value of Pi

import random

SIZE = 1000000
count = 0

for i in range(1, SIZE):
    x = random.random()
    y = random.random()

    if x*x + y*y < 1:   #test for inside of circle
        count += 1

pi = 4.0 * count / SIZE

print ("With", SIZE, "trials Pi =", pi)

##Output
##With 1000000 trials Pi = 3.141164
