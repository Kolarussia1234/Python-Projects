from tkinter import *
from tkinter.ttk import *  #Uuema valjanagemisega tkinter
from turtle import TurtleScreen, RawTurtle

#Tekitame rakendus
root = Tk()
root.title("Nuppudega Konn")
#mAARAME REA JA VEERY INDEKSIGA 0 KOIGE KAALUMATEKS
root.rowconfigure(index=0,weight=1)
root.columnconfigure(index=0,weight=1)
#Tekita louend,seo see root objektiga
c = Canvas(root, bg='green')
#Loendi nahtavaks muutmiseks paigutame ta lahtrisse 0,0
c.grid(column=0, row=0, sticky=(N, S, W, E))
#Seo loendiga TurtleScreen ja seo TurtleScreeniga konn
ts = TurtleScreen(c)
ts.bgcolor('cyan')
konn = RawTurtle(ts)
konn.color('green')

def edasi():
    konn.forward(kiirus.get())

def vasakule():
    konn.left(90)

def paremale():
    konn.right(90)


#Tekitame nuppude paneeli f
f = Frame(root)
f.grid(column=0,row=1)

#Nupp Edasi
b = Button(f, text="Edasi",command=edasi)
b.grid(column=0,row=0)


    #Tekita vasakpoorde nupp
bv = Button(f,text="Vasakule",command=vasakule)
bv.grid(column=1,row=0)


    #Tekitame parempoolse nuppu
bp= Button(f,text="Paremale",command=paremale)
bp.grid(column=2,row=0)

#Tekita tektsikast kiiruse sisestamiseks
kiirus = IntVar()
kiirus.set(100)
lbl_kiirus = Label(root,text="    Kiirus    ")
entry_kiirus=Entry(f,text="    Kiirus    ",textvariable=kiirus)
entry_kiirus.grid(column=4,row=0)


#Kaivitame rakendus
root.mainloop()
