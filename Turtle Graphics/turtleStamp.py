from turtle import Turtle

t=Turtle()
t.up()
t.setx(-50)
t.hideturtle()
t.shape('turtle')

for i in range(4):
    for i in range(4):
        t.fd(50)
        t.stamp()
    t.left(90)

t.screen.exitonclick()
