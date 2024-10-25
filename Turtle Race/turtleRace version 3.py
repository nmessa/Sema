##Turtle Race version 3
##Author: nmessa
##This version has the turtles racing around the edge of the screen
##The screen has been modified to 900 x 900 pixels.
##The victoryDance function has been modified so the turtle goes
##to the home position
##The program has also been modified such that the turtles do not draw
##when the are racing
##The program keeps track of how many pixels it has traveled in one direction
##When the number of pixels gets to 800, it turns right.  When it moves 3200
##pixels, it has completed the course

from turtle import *
from random import randint

def victoryDance(t, turns):
    t.penup()
    t.home()
    t.speed(3)
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
        
setup(900, 900)
window = Screen()

mary = Turtle()
mary.shape('turtle')
mary.speed(0)
mary.color('red')
mary.penup()
mary.goto(-400, 400)
#mary.pendown()

fred = Turtle()
fred.shape('turtle')
fred.speed(0)
fred.color('green')
fred.penup()
fred.goto(-400, 400)
#fred.pendown()

jane = Turtle()
jane.shape('turtle')
jane.speed(0)
jane.color('blue')
jane.penup()
jane.goto(-400, 400)
#jane.pendown()

jeff = Turtle()
jeff.shape('turtle')
jeff.speed(0)
jeff.color('black')
jeff.penup()
jeff.goto(-400, 400)
#jeff.pendown()

finished = False
maryCount = 0
fredCount = 0
janeCount = 0
jeffCount = 0
maryTotal = 0
fredTotal = 0
janeTotal = 0
jeffTotal = 0

while not finished:
    maryMove = randint(1, 10)
    maryCount += maryMove
    maryTotal += maryMove
    mary.forward(maryMove)

    fredMove = randint(1,10)
    fredCount += fredMove
    fredTotal += fredMove
    fred.forward(fredMove)

    janeMove = randint(1,10)
    janeCount += janeMove
    janeTotal += janeMove
    jane.forward(janeMove)

    jeffMove = randint(1,10)
    jeffCount += jeffMove
    jeffTotal += jeffMove
    jeff.forward(jeffMove)

    if maryCount >= 800:
        maryCount = 0
        mary.right(90)

    if fredCount >= 800:
        fredCount = 0
        fred.right(90)

    if janeCount >= 800:
        janeCount = 0
        jane.right(90)

    if jeffCount >= 800:
        jeffCount = 0
        jeff.right(90)

    if maryTotal >= 3200:
        finished = True
        victoryDance(mary, 5)

    if fredTotal >= 3200:
        finished = True
        victoryDance(fred, 6)

    if janeTotal >= 3200:
        finished = True
        victoryDance(jane, 7)

    if jeffTotal >= 3200:
        finished = True
        victoryDance(jeff, 8)

        
window.exitonclick()   



