from tkinter import *

window = Tk()

window.iconbitmap('computer.ico')
window.title("PC Planet")

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
window.minsize(width=300,height=200)

def openAddDoc():
    exec(open("AddDoc.py").read())

def openViewDoc():
    exec(open("ViewDoc.py").read())

titleLabel = Label(topFrame, text="Main Menu")
titleLabel.config(font=("Ariel", 12))
addButton = Button(topFrame, text="Add", command=openAddDoc, height=2, width=10)
viewButton = Button(topFrame, text="View", height=2, width=10)
deleteButton = Button(topFrame, text="Delete", height=2, width=10)
updateButton = Button(topFrame, text="Update", height=2, width=10)

titleLabel.grid(row=0, column=1, pady=12)
addButton.grid(row=1, column=0, pady=12)
viewButton.grid(row=1, column=2, pady=12)
deleteButton.grid(row=2, column=0, pady=12)
updateButton.grid(row=2, column=2, pady=12)

window.mainloop()