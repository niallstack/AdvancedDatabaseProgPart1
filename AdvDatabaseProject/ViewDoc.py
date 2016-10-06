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

def printManByManDoc(event):
    manByManDoc_list = db.view('_design/manufacturer/_view/by_manufacturer_doc')
    listbox.delete('0', END)
    for r in manByManDoc_list:
        listbox.insert(END, r)

def printManByModPri(event):
    manByModPri_list = db.view('_design/manufacturer/_view/by_model_price')
    listbox.delete('0', END)
    for r in manByModPri_list:
        listbox.insert(END, r)

def printPriByManMod(event):
    priByManMod_list = db.view('_design/video_cards/_view/by_manufacturer_model_price')
    listbox.delete('0', END)
    for r in priByManMod_list:
        listbox.insert(END, r)

def printRedByManModStock(event):
    redByManModStck_list = db.view('_design/reduce/_view/by_manufacturer_model_stock')
    listbox.delete('0', END)
    for r in redByManModStck_list:
        listbox.insert(END, r)

def printRedByManSum(event):
    redByManSum_list = db.view('_design/reduce/_view/by_manufacturer_sum')
    listbox.delete('0', END)
    for r in redByManSum_list:
        listbox.insert(END, r)


basicButton = Button(frame, text="Basic View")
compByManModButton = Button(frame, text="Components by Manufacturer and Model")
cpuByCoresDocButton = Button(frame, text="CPU by Cores and Document")
ManByManDocButton = Button(frame, text="Manufacturer by Manufacturer and Document")
ManByModPriButton = Button(frame, text="Manufacturer by Model and Price")
PriByManModButton = Button(frame, text="Price by Manufacturer and Model")
RedByManModStockButton = Button(frame, text="Reduced View by Manufacturer, Model and Stock")
RedByManSumButton = Button(frame, text="Reduced View by Manufacturer and Sum")

viewsLabel = Label(frame, text="----Views----")
viewsLabel.pack()

basicButton.bind("<Button-1>", printBasic)
compByManModButton.bind("<Button-1>", printCompByManMod)
cpuByCoresDocButton.bind("<Button-1>", printCpuByCoresDoc)
ManByManDocButton.bind("<Button-1>", printManByManDoc)
ManByModPriButton.bind("<Button-1>", printManByModPri)
PriByManModButton.bind("<Button-1>", printPriByManMod)
RedByManModStockButton.bind("<Button-1>", printRedByManModStock)
RedByManSumButton.bind("<Button-1>", printRedByManSum)

basicButton.pack()
compByManModButton.pack()
cpuByCoresDocButton.pack()
ManByManDocButton.pack()
ManByModPriButton.pack()
PriByManModButton.pack()

ReducesLabel = Label(frame, text="----Reduces----")
ReducesLabel.pack()

RedByManModStockButton.pack()
RedByManSumButton.pack()



window.mainloop()