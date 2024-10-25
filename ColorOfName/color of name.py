## Lab Exercise 12/21/2016 Problem 2
## Author: nmessa
## This program will calculate and display a window with the
## color of your name

import pygame, sys

name = input("Enter your name (First Middle Last): ")
names = name.split()

red = 0
for c in names[0]:
    red += ord(c)
red %= 256

green = 0
for c in names[1]:
    green += ord(c)
green %= 256

blue = 0
for c in names[2]:
    blue += ord(c)
blue %= 256

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([red, green, blue])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
