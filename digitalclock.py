from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
f1 =("poppins" , 24,"bold")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font = f1 , background= "black" , foreground = "cyan")
label.pack(anchor="center")

time()

mainloop()