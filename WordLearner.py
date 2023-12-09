from tkinter import *
from PIL import ImageTk, Image


class Word:
    def __init__(self, wordPL, wordEng):
        self.wordPL = wordPL
        self.wordEng = wordEng


def create_word_objects():
    words = [
        Word("kot", "cat"),
        Word("pies", "dog"),
        Word("dom", "house"),
    ]
    return words


root = Tk()
root.title("Words Learner")

wordNum = 0
correctAnswers = 0

words = create_word_objects()

label = Label(root, text=words[0].wordPL, height=1, width=30)
label.grid(row=0, column=0)

e = Entry(root, width=30, borderwidth=5)

labelCounter = Label(root, text="1/" + str(len(words)), height=1, width=10)


def submit():
    global wordNum
    global correctAnswers
    if e.get() == words[wordNum].wordEng:
        correctAnswers += 1
    wordNum += 1
    if wordNum > len(words) - 1:  # submit screen
        buttonSubmit.config(state=DISABLED)
        e.grid_forget()
        label.config(text="Correct answers: " + str(correctAnswers))
        labelCounter.grid_forget()
    else:
        label.config(text=words[wordNum].wordPL)
        e.delete(0, END)
    labelCounter.config(text=str(wordNum + 1) + "/" + str(len(words)))


buttonSubmit = Button(root, text="Submit", command=submit)
buttonSubmit.grid(row=2, column=0, pady=10)
e.grid(row=1, column=0)
labelCounter.grid(row=3, column=0)
root.mainloop()
