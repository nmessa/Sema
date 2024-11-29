#Lab Exercise 10/26/2022
#projectile.py
#Author: nmessa
#Projectile motion project
#Projectile class definition file

from math import *

class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        self.initial_height = height
        theta = pi * angle / 180.0      #convert to radians
        self.xvel = velocity * cos(theta)     # x-component of velocity
        self.yvel = velocity * sin(theta)       # y-component of velocity

    def update(self, time):
        #x = vx * t
        self.xpos = time * self.xvel
        #y = h0 + vy*t - 4.9*t*t
        self.ypos = self.initial_height + self.yvel * time - 4.9 * time**2

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos
#end of class definition
