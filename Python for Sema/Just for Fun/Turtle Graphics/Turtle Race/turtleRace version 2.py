##Turtle Race Version 2
##Author: nmessa
##This version detects when a turtle gets to an X coordinate of 400
##At this point the turtle that won the race does a victory dance
##by calling the victoryDance function.  The victoryDance function takes two
##parameters; a turtle object and the number of turns in the polygon it makes

from turtle import *
from random import randint
 
def victoryDance(t, turns):
    t.penup()
    t.goto(0, -300)
    t.pendown()
    for _ in range(turns):
        t.forward(100)
        t.left(360/turns)
    t.penup()
    for _ in range(3):
        t.left(360)
    for _ in range(3):
        t.right(360)
    for _ in range(3):
        t.left(90)
        t.forward(50)
        t.right(180)
        t.forward(50)
        t.left(90)
        
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
    if mary.xcor() > 400:
        finished = True
        victoryDance(mary, 5)
    if fred.xcor() > 400:
        finished = True
        victoryDance(fred, 6)
    if jane.xcor() > 400:
        finished = True
        victoryDance(jane, 7)
    if jeff.xcor() > 400:
        finished = True
        victoryDance(jeff, 8)
window.exitonclick()   



