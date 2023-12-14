from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()
