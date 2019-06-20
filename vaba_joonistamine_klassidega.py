from tkinter import *
from tkinter.ttk import *

class JoonistamiseApp(Tk):

    def __init__(self):
        Tk.__init__(self) # ülemklassi intsialiseerimismeetodi väljakutse
        # Tekita objektid
        self.c = Canvas(self, bg="white")
        self.koord_str = StringVar()
        self.koordinaadid = Label(self, textvariable=self.koord_str)

        # Paiguta objektid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.c.grid(row=0, column=0, sticky=(N, S, W, E))
        self.koordinaadid.grid(row=1, column=0)

        # Seosta funktsioonidega
        self.c.bind("<Button-1>", self.vasak_nupp)
        self.c.bind("<Button-2>", self.keskmine_nupp)
        self.c.bind("<Button-3>", self.parem_nupp)
        self.c.bind("<B1-Motion>", self.vasakuga_lohistamine)
        self.c.bind("<B1-ButtonRelease>", self.vasaku_vabastamine)
                
        self.alg_x = 0
        self.alg_y = 0
        self.abijoone_id = None

    def vasak_nupp(self, event):
        #global alg_x, alg_y
        self.koord_str.set("X: " + str(event.x) + ", Y: " + str(event.y))
        self.alg_x = event.x
        self.alg_y = event.y

    def keskmine_nupp(self, event):
        self.koord_str.set("X: " + str(event.x) + ", Y: " + str(event.y))
        self.c.create_line(event.x, event.y-5, event.x, event.y+5)
        self.c.create_line(event.x-5, event.y, event.x+5, event.y)

    def parem_nupp(self, event):
        self.koord_str.set("X: " + str(event.x) + ", Y: " + str(event.y))
        self.c.create_oval(event.x-5, event.y-5, event.x+5, event.y+5)
        
    def vasakuga_lohistamine(self, event):
        #global abijoone_id
        self.koord_str.set("X: " + str(event.x) + ", Y: " + str(event.y))
        self.c.delete(self.abijoone_id)
        self.abijoone_id = self.c.create_line(self.alg_x, self.alg_y, event.x, event.y)

    def vasaku_vabastamine(self, event):
        #global abijoone_id
        self.abijoone_id = None

root = JoonistamiseApp()
root.mainloop()
