from tkinter import *
import couchdb

window = Tk()

#window.iconbitmap('computer.ico')
window.title("PC Planet-View")

frame = Frame(window)
frame.pack()
window.minsize(width=700,height=600)
listbox = Listbox(frame, width=150, height=20)
listbox.pack()


server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']


def printCompByManMod(event):
    compByManMod_list = db.view('_design/components/_view/by_manufactures_model')
    listbox.delete('0', END)
    for r in compByManMod_list:
        listbox.insert(END, r)


compByManModButton = Button(frame, text="Components by Manufacturer and Model")
compByManModButton.bind("<Button-1>", printCompByManMod)
compByManModButton.pack()


window.mainloop()