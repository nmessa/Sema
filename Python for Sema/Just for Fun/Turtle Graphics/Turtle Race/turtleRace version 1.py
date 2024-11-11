##Turtle Race version 1
##Author: nmessa
##This version creates 4 turtles and they race across the screen

from turtle import *
from random import randint 

window = Screen()

mary = Turtle()
mary.shape('turtle')
mary.color('red')
mary.penup()
mary.goto(-360, 100)
mary.pendown()

fred = Turtle()
fred.shape('turtle')
fred.color('green')
fred.penup()
fred.goto(-360, 70)
fred.pendown()

jane = Turtle()
jane.shape('turtle')
jane.color('blue')
jane.penup()
jane.goto(-360, 40)
jane.pendown()

jeff = Turtle()
jeff.shape('turtle')
jeff.color('black')
jeff.penup()
jeff.goto(-360, 10)
jeff.pendown()

finished = False
while not finished:
    mary.forward(randint(1,10))
    fred.forward(randint(1,10))
    jane.forward(randint(1,10))
    jeff.forward(randint(1,10))
    
window.exitonclick()   #this line never executes



