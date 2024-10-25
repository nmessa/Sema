##Alien Interaction - Version 2
##Author: nmessa
##Date: 12.15.2023

from tkinter import *

#Define alien functions
def mouth_open():
    c.itemconfig(mouth, fill = 'black')

def mouth_close():
    c.itemconfig(mouth, fill = 'red')

def blink():
    c.itemconfig(eye, fill = 'green')
    c.itemconfig(eyeball, state = HIDDEN)

def unblink():
    c.itemconfig(eye, fill = 'white')
    c.itemconfig(eyeball, state = NORMAL)

def steal_hat():
    c.itemconfig(hat, state = HIDDEN)
    c.itemconfig(words, text = "Give me back my hat!")

def return_hat():
    c.itemconfig(hat, state = NORMAL)
    c.itemconfig(words, text = "Thank you!!!")
    
#Setup window and canvas
window = Tk()
window.title("Alien")
c = Canvas(window, height = 300, width = 400)
c.pack()

#Draw alien body parts
body = c.create_oval(100, 150, 300, 250, fill = 'green')
eye = c.create_oval(170, 70, 230, 130, fill = 'white')
eyeball = c.create_oval(190, 90, 210, 110, fill = 'black')
mouth = c.create_oval(150, 220, 250, 240, fill = 'red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill = 'blue')
words = c.create_text(200, 280, text = "I am an alien")
