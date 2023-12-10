from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("New Window")


def open():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    my_img = ImageTk.PhotoImage(Image.open("images/Bez_nazwy.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
