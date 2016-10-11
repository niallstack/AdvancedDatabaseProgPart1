from tkinter import *
import couchdb

#Creates GUI window
window = Tk()

#Adding icon and title to the window
window.iconbitmap('computer.ico')
window.title("PC Planet - Views")

#Creating a frame in the window
frame = Frame(window)
frame.pack()
window.minsize(width=700,height=600)

#Adding a listbox
listbox = Listbox(frame, width=150, height=20)
listbox.pack()

#Connecting to the Database
server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

#All these functions output various views to the listbox
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


#Creating the buttons
basicButton = Button(frame, text="Basic View")
compByManModButton = Button(frame, text="Components by Manufacturer and Model")
cpuByCoresDocButton = Button(frame, text="CPU by Cores and Document")
ManByManDocButton = Button(frame, text="Manufacturer by Manufacturer and Document")
ManByModPriButton = Button(frame, text="Manufacturer by Model and Price")
PriByManModButton = Button(frame, text="Price by Manufacturer and Model")
RedByManModStockButton = Button(frame, text="Reduced View by Manufacturer, Model and Stock")
RedByManSumButton = Button(frame, text="Reduced View by Manufacturer and Sum")

#Creating labels
viewsLabel = Label(frame, text="Views")
viewsLabel.config(font=("Ariel", 12))
viewsLabel.pack(pady=12)

#Connecting the buttons to functions
basicButton.bind("<Button-1>", printBasic)
compByManModButton.bind("<Button-1>", printCompByManMod)
cpuByCoresDocButton.bind("<Button-1>", printCpuByCoresDoc)
ManByManDocButton.bind("<Button-1>", printManByManDoc)
ManByModPriButton.bind("<Button-1>", printManByModPri)
PriByManModButton.bind("<Button-1>", printPriByManMod)
RedByManModStockButton.bind("<Button-1>", printRedByManModStock)
RedByManSumButton.bind("<Button-1>", printRedByManSum)

#Adding the buttons to the frame
basicButton.pack()
compByManModButton.pack()
cpuByCoresDocButton.pack()
ManByManDocButton.pack()
ManByModPriButton.pack()
PriByManModButton.pack()
RedByManModStockButton.pack()
RedByManSumButton.pack()

window.mainloop()