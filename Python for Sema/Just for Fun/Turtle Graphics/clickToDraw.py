##clickToDraw.py
##Author: nmessa
##Date: 6.15.2015

from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.color("orange")
t.shape('turtle')
t.shapesize(4)

def circle(x,y):
    t.circle(200)

t.onclick(circle)


