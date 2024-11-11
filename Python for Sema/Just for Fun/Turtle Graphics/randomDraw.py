##randomDraw.py
##Author: nmessa
##Date: 6.15.2015

from turtle import Turtle
import random

t=Turtle()
t.screen.bgcolor("black")
t.speed(0)

def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(["blue","red","green"]))
        random.choice([right,left])
        t.fd(distance)

random_drawing(100,50)
t.screen.exitonclick()
