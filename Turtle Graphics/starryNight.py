import turtle as t
from random import *

def drawStar(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180//points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

t.Screen().bgcolor('dark blue')
t.speed(0)

while True:
    randPoints = randint(2, 5) * 2 + 1
    randSize = randint(10, 50)
    randCol = (random(), random(), random())
    randX = randint(-350, 300)
    randY = randint(-250, 250)
    drawStar(randPoints, randSize, randCol, randX, randY)
