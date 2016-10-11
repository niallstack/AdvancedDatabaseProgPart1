from tkinter import *
import couchdb

#Creates GUI window
window = Tk()

#Adding icon and title to the window
window.iconbitmap('computer.ico')
window.title("PC Planet - Views")

#Creating a frame in the window
frame = Frame(window)
frame.grid()
window.minsize(width=700,height=600)

#Adding a listbox
listbox = Listbox(frame, width=150, height=20)
listbox.grid(row=1, column=0)

#Connecting to the Database
server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

#Creating a map function
map_fun = '''function(doc) {
         emit(doc.manufacturer,doc.stockCount)
}'''
#Delteing entries in the listbox
listbox.delete('0', END)
for row in db.query(map_fun):
    listbox.insert(END, row.key)
    listbox.insert(END, row.value)

#This function adds a reduce to the map function
def reduceOn(event):
    listbox.delete('0', END)

    map_fun = '''function(doc) {
             emit(doc.manufacturer,doc.stockCount)
    }'''

    red_fun = '''function(keys, values) {
                    var stats = {
                    models: 0,
                    stock: 0
                    };
                stats.models = values.length;
                stats.stock = sum(values);

                return stats;
            }'''
    for row in db.query(map_fun, red_fun):
        listbox.insert(END, row.key)
        listbox.insert(END, row.value)

#Creating, Adding and connectiong the button to the reduceOn function
reduceButton = Button(frame, text="Reduce")
reduceButton.grid(row=2, column=0)
reduceButton.bind("<Button-1>", reduceOn)


window.mainloop()