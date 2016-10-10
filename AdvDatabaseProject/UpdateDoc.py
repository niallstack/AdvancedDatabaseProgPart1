from tkinter import *
import couchdb

window = Tk()

window.iconbitmap('computer.ico')
window.title("PC Planet")

server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

frame = Frame(window)
frame.pack()
window.minsize(width=700,height=600)
listbox = Listbox(frame, width=150, height=20)
listbox.grid(row=0, column=0)

compByManMod_list = db.view('_design/components/_view/by_manufactures_model')
listbox.delete('0', END)
for r in compByManMod_list:
    listbox.insert(END, r)

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
labelID.grid(row=1, column=0)
labelRev.grid(row=2, column=0)
labelComponent.grid(row=3, column=0)
labelManufacturer.grid(row=4, column=0)
labelModel.grid(row=5, column=0)

entryID.grid(row=1, column=1)
entryRev.grid(row=2, column=1)
entryComponent.grid(row=2, column=1)
entryManufacturer.grid(row=3, column=1)
entryModel.grid(row=4, column=1)
button.grid(row=5, column=1)


def on_button(event):
    couch = couchdb.Server()
    couch = couchdb.Server('http://127.0.0.1:5984/')
    db = couch['pcparts']
    doc = {'component': entryComponent.get(), 'manufacturer': entryManufacturer.get(), 'model': entryModel.get()}
    db.save(doc)
    entryComponent.delete(0, 'end')
    entryModel.delete(0, 'end')
    entryManufacturer.delete(0, 'end')

button.bind("<Button-1>", on_button)



window.mainloop()