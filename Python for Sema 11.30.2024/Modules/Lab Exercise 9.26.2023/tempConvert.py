#Demonstration of use of modules
#Author: nmessa
#Date: 9.26.2023

import my_module
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print ("That's", fahrenheit, "degrees Fahrenheit")
