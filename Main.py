from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons, Images and Exit Buttons")
# root.iconbitmap("C:/Users/Juliao JM/Downloads/py-white.ico")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("fryc.png"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()