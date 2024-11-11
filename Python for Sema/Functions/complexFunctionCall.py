## Lab Exercise 10/7/2024 Problem 1
## Author: nmessa
## This program demonstrates a complex function call
import math

def f(x):
    return g(x) + math.sqrt(h(x))

def g(x):
    return 4 * h(x)

def h(x):
    return x * x + k(x) -1

def k(x):
    return 2 * (x+1)

print (f(2)) #39.0
