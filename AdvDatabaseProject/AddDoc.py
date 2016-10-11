from tkinter import *
import couchdb

#Creating GUI window
window = Tk()

#Adding icon and title to the window
window.iconbitmap('computer.ico')
window.title("PC Planet")

#Creating a frame in the window
frame = Frame(window)
frame.pack()

#Creating and adding labels, text fields and buttons to the frame
labelComponent = Label(frame, text="Component:")
labelManufacturer = Label(frame, text="Manufacturer:")
labelModel = Label(frame, text="Model:")
entryComponent = Entry(frame)
entryManufacturer = Entry(frame)
entryModel = Entry(frame)
button = Button(frame, text="Enter")
labelComponent.grid(row=0, column=0)
labelManufacturer.grid(row=1, column=0)
labelModel.grid(row=2, column=0)

entryComponent.grid(row=0, column=1)
entryManufacturer.grid(row=1, column=1)
entryModel.grid(row=2, column=1)
button.grid(row=3, column=1)

#A function that connects to the database then saves a document to it
def on_button(event):
    couch = couchdb.Server()
    couch = couchdb.Server('http://127.0.0.1:5984/')
    db = couch['pcparts']
    doc = {'component': entryComponent.get(), 'manufacturer': entryManufacturer.get(), 'model': entryModel.get()}
    db.save(doc)
    entryComponent.delete(0, 'end')
    entryModel.delete(0, 'end')
    entryManufacturer.delete(0, 'end')

#This connects the button to the on_button function
button.bind("<Button-1>", on_button)



window.mainloop()