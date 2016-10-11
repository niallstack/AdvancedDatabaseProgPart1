from tkinter import *
import couchdb

#Creates GUI window
window = Tk()

#Adding icon and title to the window
window.iconbitmap('computer.ico')
window.title("PC Planet - Delete")

#Creating a frame in the window
frame = Frame(window)
frame.pack()
window.minsize(width=700,height=600)

#Adding a listbox
listbox = Listbox(frame, width=150, height=20)
listbox.grid(row=0, column=0)

#Connecting to the Database
server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

#This function adds a view of the database to the listbox
def printCompByManMod(event):
    compByManMod_list = db.view('_design/components/_view/by_manufactures_model')
    listbox.delete('0', END)
    for r in compByManMod_list:
        listbox.insert(END, r)

#Creating the label and textbox
labelID = Label(frame, text="ID:")
entryID = Entry(frame)

#Adding the label and textbox to the frame
labelID.grid(row=2, column=0)
entryID.grid(row=3, column=0)

#This function deletes a document by its ID number
def deleteDoc(event):
    couch = couchdb.Server()
    couch = couchdb.Server('http://127.0.0.1:5984/')
    db = couch['pcparts']
    id = entryID.get()
    del db[id]
    entryID.delete(0, 'end')

#Creating, adding and connecting the two buttons to their functions
compByManModButton = Button(frame, text="Components by Manufacturer and Model")
compByManModButton.bind("<Button-1>", printCompByManMod)
compByManModButton.grid(row=1, column=0, pady=20)
deleteButton = Button(frame, text="Delete")
deleteButton.bind("<Button-1>", deleteDoc)
deleteButton.grid(row=4,column=0)


window.mainloop()