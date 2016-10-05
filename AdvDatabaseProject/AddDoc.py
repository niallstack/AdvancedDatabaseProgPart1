import tkinter as tk
import couchdb

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.labelComponent = tk.Label(self, text="Component:")
        self.labelManufacturer = tk.Label(self, text="Manufacturer:")
        self.labelModel = tk.Label(self, text="Model:")
        self.entryComponent = tk.Entry(self)
        self.entryManufacturer = tk.Entry(self)
        self.entryModel = tk.Entry(self)
        self.button = tk.Button(self, text="Enter", command=self.on_button)
        #self.button.pack()

        #self.entryComponent.pack()
        self.labelComponent.grid(row=0, column=0)
        self.labelManufacturer.grid(row=1, column=0)
        self.labelModel.grid(row=2, column=0)

        self.entryComponent.grid(row=0, column=1)
        self.entryManufacturer.grid(row=1, column=1)
        self.entryModel.grid(row=2, column=1)
        self.button.grid(row=3, column=1)

    def on_button(self):
        couch = couchdb.Server()
        couch = couchdb.Server('http://127.0.0.1:5984/')
        db = couch['pcparts']
        doc = {'component': self.entryComponent.get(), 'manufacturer': self.entryManufacturer.get(), 'model': self.entryModel.get()}
        db.save(doc)

w = SampleApp()
w.iconbitmap('computer.ico')
w.title("PC Planet-Add")
w.mainloop()