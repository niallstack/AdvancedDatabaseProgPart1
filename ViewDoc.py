from tkinter import *
import couchdb

window = Tk()

#window.iconbitmap('computer.ico')
window.title("PC Planet-View")

frame = Frame(window)
frame.pack()
window.minsize(width=600,height=600)

server = couchdb.client.Server('http://127.0.0.1:5984/')
db = server['pcparts']

restaurant_list = db.view('_all_docs')
for r in restaurant_list :
    print(r)

window.mainloop()