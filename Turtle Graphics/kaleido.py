import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def drawCircle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    drawCircle(size+5, angle+1, shift+1)

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(4)
drawCircle(30, 0, 1)
