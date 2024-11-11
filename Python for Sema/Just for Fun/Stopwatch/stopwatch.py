##stopwatch.py
##Author: nmessa
##Date: 2.22.2024
##THis program will acts as a stopwatch for timing events

from random import *
from time import *

print("Welcome to the Computer Stopwatch")
print("Hit ENTER to start the timer and hit ENTER again to stop the timer")

#Start the stopwatch
input("Start >> ")

#Get time from system clock
start_time = time()

#Stop the stopwatch
input("Stop >> ")

#Get time from system clock
end_time = time()

#Calculate elapsed_time in seconds
elapsed_time = end_time - start_time

#round elapsed_time to 2 decimal places
elapsed_time = round(elapsed_time, 2)

#print the result
print(elapsed_time, "seconds")
