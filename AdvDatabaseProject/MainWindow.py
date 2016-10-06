from tkinter import *

window = Tk()

window.iconbitmap('computer.ico')
window.title("PC Planet")

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
window.minsize(width=600,height=200)

def openAddDoc():
    exec(open("AddDoc.py").read())

def openViewDoc():
    exec(open("ViewDoc.py").read())

titleLabel = Label(topFrame, text="PC Planet")
titleLabel.config(font=("Ariel", 44))
addButton = Button(topFrame, text="Add", command=openAddDoc, height=2, width=10)
viewButton = Button(topFrame, text="View", height=2, width=10)
deleteButton = Button(topFrame, text="Delete", height=2, width=10)

titleLabel.grid(row=0, column=2)
addButton.grid(row=1, column=1)
viewButton.grid(row=1, column=2)
deleteButton.grid(row=1, column=3)

window.mainloop()