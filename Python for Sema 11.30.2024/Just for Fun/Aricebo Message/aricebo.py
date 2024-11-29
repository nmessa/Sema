##Aricebo Message Decoder
##Author: nmessa
##Date: 12/19/2022
##This utilizes the Rance Necaise graphics library

from graphics import *

#Create Graphic Window and Canvas to draw on
win = GraphicsWindow(800, 800)
canvas = win.canvas()

#Define start position of graphic
x = 300
y = 25

#Define "pixel" size
height = 10
width = 10

#define colors
colors = ['black', 'white']

#Open message file and read in all lines
myFile = open("message.dat", "r")
lines = myFile.readlines()
myFile.close()

#Draw the graphic
for line in lines:
    for col in range(len(line)-1):
        if line[col] != '\n':
            canvas.setColor(colors[int(line[col])])
        canvas.drawRect(x, y, width, height)
        x += width
    y += height
    x = 300

win.wait()
    
