from tkinter import *

def A():
    print("Thank you!")
    
def B():
    print("Ouch! That hurt!")

window = Tk()
buttonA = Button(window, text = "Press Me!", command = A)
buttonB = Button(window, text = "Don\'t press!", command = B)
buttonA.pack()
buttonB.pack()
