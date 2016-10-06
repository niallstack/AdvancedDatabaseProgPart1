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


def printBasic(event):
    basic_list = db.view('_all_docs')
    listbox.delete('0', END)
    for r in basic_list:
        listbox.insert(END, r)

def printCompByManMod(event):
    compByManMod_list = db.view('_design/components/_view/by_manufactures_model')
    listbox.delete('0', END)
    for r in compByManMod_list:
        listbox.insert(END, r)

def printCpuByCoresDoc(event):
    cpuByCoresDoc_list = db.view('_design/cpu/_view/by_cores_doc')
    listbox.delete('0', END)
    for r in cpuByCoresDoc_list:
        listbox.insert(END, r)

basicButton = Button(frame, text="Basic View")
compByManModButton = Button(frame, text="Components By Manufacturer and Model")
cpuByCoresDocButton = Button(frame, text="CPU By Cores and Document")
basicButton.bind("<Button-1>", printBasic)
compByManModButton.bind("<Button-1>", printCompByManMod)
cpuByCoresDocButton.bind("<Button-1>", printCpuByCoresDoc)
basicButton.pack()
compByManModButton.pack()
cpuByCoresDocButton.pack()

window.mainloop()