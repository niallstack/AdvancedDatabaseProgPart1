from tkinter import *
import couchdb

window = Tk()

window.iconbitmap('computer.ico')
window.title("PC Planet - Views")

frame = Frame(window)
#frame.pack()
frame.grid()
window.minsize(width=700,height=600)
listbox = Listbox(frame, width=150, height=20)
listbox.grid(row=1, column=0)


server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

map_fun = '''function(doc) {
         emit(doc.manufacturer,doc.stockCount)
}'''
listbox.delete('0', END)
for row in db.query(map_fun):
    listbox.insert(END, row.key)
    listbox.insert(END, row.value)


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

#def tempMap():
#    map_fun = '''function(doc) {
#        if (doc.component == 'Video Card')
#            emit(doc.component, {Manufacturer: doc.manufacturer, Model: doc.model});
#    }'''
#    for row in db.query(map_fun):
#        listbox.insert(END, r)

reduceButton = Button(frame, text="Reduce")
reduceButton.grid(row=2, column=0)
reduceButton.bind("<Button-1>", reduceOn)


window.mainloop()