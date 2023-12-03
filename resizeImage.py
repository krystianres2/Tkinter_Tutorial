from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons, Images and Exit Buttons")
root.geometry("1000x500")

my_pic = Image.open("image.png")
width = 200
height = 350

resized = my_pic.resize((width, height), Image.Resampling.LANCZOS)

new_pic = ImageTk.PhotoImage(resized)


def resize():
    global my_pic
    global new_pic
    my_pic = Image.open("image.png")
    global width
    width += 50
    resized = my_pic.resize((width, height), Image.Resampling.LANCZOS)
    new_pic = ImageTk.PhotoImage(resized)
    my_label.config(image=new_pic)


button_resize = Button(root, text="Feed me", padx=10, pady=10, command=resize)

button_resize.pack(pady=20)
my_label = Label(root, image=new_pic)
my_label.pack(pady=20)

root.mainloop()
