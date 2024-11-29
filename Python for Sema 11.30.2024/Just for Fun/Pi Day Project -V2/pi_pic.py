##Pi Picture Painter
##Author: nmessa
##Date: 3/14/2023
##This utilizes the Rance Necaise graphics library

from graphics import *

#Create Graphic Window and Canvas to draw on
win = GraphicsWindow(1000, 1000)
canvas = win.canvas()

#Define start position of graphic
x = 0
y = 0

#Define "pixel" size
#use 100x100 for 100 digits of pi
#use 10x10 for 10000 digits of pi
#use 4x4 for 62500 digits of pi
#use 2x2 for  250000 digits of pi
height = 10
width = 10

#define colors
colors = ['red', 'blue', 'orange', 'magenta', 'yellow', 'purple', 'salmon',
          'lime', 'aquamarine', 'cyan' ]

#Open message file and read in all lines
myFile = open("pi_million_digits.txt", "r")
lines = myFile.readlines()
myFile.close()
temp = ""

#Get rid of newline characters
for line in lines:
    temp += line.rstrip()
    
#print(len(temp))
numbers = "0123456789"

#Build pi string
myPi = "3"
myPi += temp[2:]

#print(len(myPi))
#print(myPi[:300])

#Get rid of spaces in pi string
myPi2 = ""
for ch in myPi:
    if ch != ' ':
        myPi2 += ch
        
#print(myPi2[:300])
        
index = 0
#Draw the graphic
for line in range(1000):
    for col in range(1000):
        #if myPi[index] in numbers:
        canvas.setColor(colors[int(myPi2[index])])
        canvas.drawRect(x, y, width, height)
        x += width
        index += 1
    y += height
    x = 0

win.wait()
    
