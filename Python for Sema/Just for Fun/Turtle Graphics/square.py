##square.py
##Author: nmessa
##Date: 6.15.2015

from turtle import Turtle
 
t=Turtle()
t.screen.bgcolor("black")
colors=["blue","purple","red","yellow"]
t.screen.tracer(0,0)
 
for x in range(360):
    t.color(colors[x%4])
    t.fd(x)
    t.left(90)
 
t.screen.exitonclick()
