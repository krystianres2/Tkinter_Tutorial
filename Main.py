from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion("this is my popup", "Hello World!")
    Label(root, text=response).pack()
    # if response == "yes":
    #     Label(root, text="You clicked Yes!").pack()
    # else:
    #     Label(root, text="You clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()
