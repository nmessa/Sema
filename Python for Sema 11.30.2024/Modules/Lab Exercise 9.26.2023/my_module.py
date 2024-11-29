## my_module.py
## Author: nmessa
## Date: 9.26.2023
## This module contains a variety of functions

import random, time

def c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def f_to_c(fahrenheit):
    celsius = 5.0 / 9 * (fahrenheit - 32)
    return celsius

def five_random():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 20))
    print (numbers)

def random_decimals():
    for i in range(10):
        print (random.random())
        time.sleep(3)



