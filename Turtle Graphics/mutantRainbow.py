import turtle as t
import random

def getLineLength():
    choice = input('Enter line length (long, medium, short): ')
    if choice == 'long':
        lineLength = 250
    elif choice == 'medium':
        lineLength = 200
    else:
        lineLength = 100
    return lineLength

def getLineWidth():
    choice = input('Enter line width (superthick, thick, thin): ')
    if choice == 'superthick':
        lineWidth = 40
    elif choice == 'thick':
        lineWidth = 25
    else:
        lineWidth = 10
    return lineWidth

def insideWindow():
    leftLimit = (-t.window_width() // 2) + 100
    rightLimit = (t.window_width() // 2) - 100
    topLimit = (t.window_width() // 2)- 100
    bottomLimit = (-t.window_width() // 2)+ 100
    (x, y) = t.pos()
    inside = leftLimit < x < rightLimit and bottomLimit < y < topLimit
    return inside

def moveTurtle(lineLength):
    penColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    t.pencolor(random.choice(penColors))
    if insideWindow():
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(lineLength)
    else:
        t.backward(lineLength)

lineLength = getLineLength()
lineWidth = getLineWidth()

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed(0)
t.pensize(lineWidth)

while True:
    moveTurtle(lineLength)



    
