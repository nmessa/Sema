## Graphing Program
## Author: nmessa
## Date: 10/9/2015
## Revision 1 - 10/10/2015 - draw the points as small circles
## This program will draw the Cartesian Coordinate system for point plotting
## This will also label points, draw a line between the points and
## calculate slope and distance of the line
## Revision 2 -  10/12/15 add the equation of the line
## Revision 3 - 10/13/2015 draws the complete line

from graphics import *
from math import *

#This function displays the point
def genMessage(p):
    message = '(' + str(round(p.x,1)) + ', ' + str(round(p.y,1)) + ')'
    coords = Text(Point(p.x, p.y-0.4), message)
    coords.draw(win)
    #draw a small circle at the location of the point
    pt = Circle(p,0.05)
    pt.setFill('red')
    pt.setOutline('red')
    pt.draw(win)

#This function generates the coordinate system
def genAxis():
    x_axis = Line(Point(-10, 0), Point(10, 0))
    x_axis.draw(win)
    y_axis = Line(Point(0, -10), Point(0, 10))
    y_axis.draw(win)
    msg1 = Text(Point(-9.5, 0.5), 'X')
    msg1.draw(win)
    msg2 = Text(Point(0.5, 9.5), 'Y')
    msg2.draw(win)
    for i in range(-9, 10):
        msg = Text(Point(0.3, i), str(i))
        msg.draw(win)
    for i in range(-9, 10):
        msg = Text(Point(i, 0.3), str(i))
        msg.draw(win)

#create the graphics window    
win = GraphWin("Graph Paper", 1000, 1000)
win.setCoords(-10.0, -10.0, 10.0, 10.0)
win.setBackground('White')
genAxis()

#plot two points
p1 = win.getMouse()
genMessage(p1)
p2 = win.getMouse()
genMessage(p2)

#draw line between two points
##myLine = Line(p1, p2)
##myLine.draw(win)

#calculate slope, distance, and y-intercept of line
m = round(1.0*(p1.y-p2.y)/(p1.x-p2.x),2)
distance = round(sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2),2)
b = round(p1.y - m*p1.x, 2)


#display slope, distance, and equation of line
msg3 = Text(Point(-8,8), 'Slope = ' + str(m))
msg4 = Text(Point(-8,7), 'Distance = ' + str(distance))
msg5 = Text(Point(-8,6), 'Y = ' + str(m) + 'X + ' + str(b)) 
msg3.draw(win)
msg4.draw(win)
msg5.draw(win)

#Plot the complete line
x1 = -9.9
x2 = 9.9
y1 = m * x1 + b
y2 = m * x2 + b
## Print new coordinates to make sure Line will still work outside
## the GraphicWindow
##print x1, y1
##print x2, y2
p3 = Point(x1, y1)
p4 = Point(x2, y2)
myLine = Line(p3, p4)
myLine.draw(win)

##for i in range(10):
##    p1 = win.getMouse()
##    genMessage(p1)
    
#wait to close window
win.getMouse()
win.close()
