from tkinter import *
from tkinter.ttk import * # Uuema väljanägemisega GUI vidinad
from turtle import TurtleScreen, RawTurtle
from frog_oop import Frog


class KonnaRakendus(Frame):
    """Frame, mida saab suvalises teises rakenduses kasutada"""

    def __init__(self, parent):
        super().__init__(parent) # Sisuliselt sama kui Tk()
        
        # Määrame rea ja veeru indeksiga 0 kõige kaalukamateks
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # Tekita lõuend, seo see root objektiga
        c = Canvas(self)
        # Lõuendi nähtavaks muutmiseks paigutame ta lahtrisse 0,0
        c.grid(column=0, row=0, sticky=(N, S, W, E))
        # Seo lõuendiga TurtleScreen ja seo TurtleScreeniga konn
        self.ts = TurtleScreen(c)
        self.algseis()

        # Tekitame nuppude paneeli f
        f = Frame(self)
        f.grid(column=0, row=1)

        # Tekita edasiliikumise nupp
        b = Button(f, text="Edasi", command=self.edasi)
        b.grid(column=0, row=0)

        # Tekita vasakpöörde nupp
        bv = Button(f, text="Vasakule", command=self.vasakule)
        bv.grid(column=1, row=0)

        # Tekita parempöörde nupp
        bp = Button(f, text="Paremale", command=self.paremale)
        bp.grid(column=2, row=0)

        # Tekita muutuja kiirus ja sildiga tekstikast kiiruse sisestamiseks
        self.kiirus = IntVar()
        self.kiirus.set(100)
        lbl_kiirus = Label(f, text="    Kiirus:   ")
        lbl_kiirus.grid(column=3, row=0)
        entry_kiirus = Entry(f, textvariable=self.kiirus)
        entry_kiirus.grid(column=4, row=0)

        # Tekita algseisu nupp
        ba = Button(f, text="Algseis", command=self.algseis)
        ba.grid(column=5, row=0)


    def algseis(self):
        self.ts.clear()
        self.ts.bgcolor('cyan')
        self.konn = Frog(self.ts, x=0, y=0)

    def edasi(self):
        self.konn.forward(self.kiirus.get()/2)
        self.konn.jump(self.kiirus.get()/2)

    def vasakule(self):
        self.konn.left(10)

    def paremale(self):
        self.konn.right(10)
        
if __name__ == '__main__':
    # Tekita rakendus
    root = Tk()
    root.title("Nuppudega konn")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    rakendus = KonnaRakendus(root)
    rakendus.grid(row=0, column=0, sticky=(N, S, W, E))
     
    # Käivita rakendus
    root.mainloop()











