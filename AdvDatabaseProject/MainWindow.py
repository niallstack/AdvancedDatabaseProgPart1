from tkinter import *
#Creating the GUI
window = Tk()

#Adding icon and title for the GUI
window.iconbitmap('computer.ico')
window.title("PC Planet")

#Creating a frame
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
window.minsize(width=300,height=200)

#Creating a link between windows
def openAddDoc():
    window.destroy()
    exec(open("AddDoc.py").read())

def openViewDoc():
    window.destroy()
    exec(open("ViewDoc.py").read())

def openDeleteDoc():
    window.destroy()
    exec(open("DeleteDoc.py").read())

def openUpdateDoc():
    window.destroy()
    exec(open("UpdateDoc.py").read())

#Creating labels and buttons that execute functions
titleLabel = Label(topFrame, text="Main Menu")
titleLabel.config(font=("Ariel", 12))
addButton = Button(topFrame, text="Add", command=openAddDoc, height=2, width=10)
viewButton = Button(topFrame, text="View", command=openViewDoc, height=2, width=10)
deleteButton = Button(topFrame, text="Delete", command=openDeleteDoc, height=2, width=10)
updateButton = Button(topFrame, text="Update", command=openUpdateDoc, height=2, width=10)

#Adding the labels and buttons to the window
titleLabel.grid(row=0, column=1, pady=12)
addButton.grid(row=1, column=0, pady=12)
viewButton.grid(row=1, column=2, pady=12)
deleteButton.grid(row=2, column=0, pady=12)
updateButton.grid(row=2, column=2, pady=12)

window.mainloop()