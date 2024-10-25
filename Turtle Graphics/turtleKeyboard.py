from turtle import Turtle
t=Turtle()

def up():
    if not(t.heading() == 90):
        t.setheading(90)
        t.fd(50)
    else:
        t.fd(50)
    
def down():
    if not(t.heading() == 270):
        t.setheading(270)
        t.fd(50)
    else:
        t.fd(50)
    
def right():
    if not (t.heading() == 0):
        t.setheading(0)
        t.fd(50)
    else:
        t.fd(50)
    
def left():
    if not (t.heading() ==180):
        t.setheading(180)
        t.fd(50)
    else:
        t.fd(50)

def undo_button():
    t.undo()

def pen_up():
    t.penup()

def pen_down():
    t.pendown()
        
def keyboard_commands():
    t.screen.onkey(up,"Up")
    t.screen.onkey(down,"Down")
    t.screen.onkey(right,"Right")
    t.screen.onkey(left,"Left")
    t.screen.onkey(undo_button,"End")
    t.screen.onkey(pen_up,"u")
    t.screen.onkey(pen_down,"d")
    t.screen.listen()

keyboard_commands()
