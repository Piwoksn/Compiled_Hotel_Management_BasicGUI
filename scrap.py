from tkinter import *

window = Tk()

def keys(event):
    label.config(text= event.keysym)

def mouse(event):
    label.config(text= f"{event.x} {event.y}")

window.bind("<Key>", keys)

window.bind("<Motion>", mouse)

window.geometry("500x500")

label = Label(window, font=("times new roman", 25, "bold"))
label.pack()





window.mainloop()