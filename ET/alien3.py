##Alien Interaction - Version 3
##Author: nmessa
##Date: 12.15.2023

from tkinter import *

#define alien functions
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

#define alien event handlers
def mouth_open2(event):
    c.itemconfig(mouth, fill = 'black')

def mouth_close2(event):
    c.itemconfig(mouth, fill = 'red')

def blink2(event):
    c.itemconfig(eye, fill = 'green')
    c.itemconfig(eyeball, state = HIDDEN)

def unblink2(event):
    c.itemconfig(eye, fill = 'white')
    c.itemconfig(eyeball, state = NORMAL)

def steal_hat2(event):
    c.itemconfig(hat, state = HIDDEN)
    c.itemconfig(words, text = "Give me back my hat!")

def return_hat2(event):
    c.itemconfig(hat, state = NORMAL)
    c.itemconfig(words, text = "Thank you!!!")
    
def eye_control(event):
    key = event.keysym
    if key == 'Up':
        c.move(eyeball, 0, -1)
    elif key == 'Down':
        c.move(eyeball, 0, 1)
    elif key == 'Left':
        c.move(eyeball, -1, 0)
    elif key == 'Right':
        c.move(eyeball, 1, 0)

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

#bind keys to event handlers
c.bind_all('<Key>', eye_control)
c.bind_all('<KeyPress-b>', blink2)
c.bind_all('<KeyPress-u>', unblink2)
c.bind_all('<KeyPress-o>', mouth_open2)
c.bind_all('<KeyPress-c>', mouth_close2)
c.bind_all('<KeyPress-s>', steal_hat2)
c.bind_all('<KeyPress-r>', return_hat2)

