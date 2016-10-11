from tkinter import *
import couchdb

#Creates GUI window
window = Tk()

#Adding icon and title to the window
window.iconbitmap('computer.ico')
window.title("PC Planet - Update")

#Connecting to the Database
server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

#Creating a frame in the window
frame = Frame(window)
frame.pack()
window.minsize(width=500, height=600)

#Adding a listbox
listbox = Listbox(frame, width=200, height=20)
listbox.grid(row=0, column=0)

#Adds a view to the listbox
compByManMod_list = db.view('_design/id/_view/by_revision_components_manufacturer_model')
listbox.delete('0', END)
for r in compByManMod_list:
    listbox.insert(END, r)

#Creating labels and buttons
labelID = Label(frame, text="ID:")
labelRev = Label(frame, text="Rev:")
labelComponent = Label(frame, text="Component:")
labelManufacturer = Label(frame, text="Manufacturer:")
labelModel = Label(frame, text="Model:")
entryID = Entry(frame)
entryRev = Entry(frame)
entryComponent = Entry(frame)
entryManufacturer = Entry(frame)
entryModel = Entry(frame)
button = Button(frame, text="Enter")

#Adding the labels and buttons to the frame
labelID.grid(row=1, column=0)
labelRev.grid(row=3, column=0)
labelComponent.grid(row=5, column=0)
labelManufacturer.grid(row=7, column=0)
labelModel.grid(row=9, column=0)
entryID.grid(row=2, column=0)
entryRev.grid(row=4, column=0)
entryComponent.grid(row=6, column=0)
entryManufacturer.grid(row=8, column=0)
entryModel.grid(row=10, column=0)
button.grid(row=12, column=0)

#A function that edits a document in the database
def on_button(event):
    couch = couchdb.Server()
    couch = couchdb.Server('http://127.0.0.1:5984/')
    db = couch['pcparts']
    doc = {'_id': entryID.get(), '_rev': entryRev.get(), 'component': entryComponent.get(), 'manufacturer': entryManufacturer.get(), 'model': entryModel.get()}
    db.save(doc)
    entryComponent.delete(0, 'end')
    entryModel.delete(0, 'end')
    entryManufacturer.delete(0, 'end')

#Connecting the button to the on_button function
button.bind("<Button-1>", on_button)


window.mainloop()