from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click me", command=myClick, fg="blue", bg="red")
myButton.pack()


root.mainloop()