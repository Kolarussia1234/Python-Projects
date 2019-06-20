from tkinter import *


root = Tk()
var_tekst = StringVar()
ent_tekst = Entry(root, textvariable=var_tekst)
ent_tekst.grid(column=0,row=0)
#Tee pikkuse Entry
var_pikkus = IntVar()
ent_pikkus = Entry(root, textvariable=var_pikkus)
ent_pikkus.grid(column=0,row=1)
#Tee nupp
def leia_pikkus():
    var_pikkus.set(len(var_tekst.get()))

    
btn_pikkus = Button(root,text="Leia pikkus",command=leia_pikkus)
btn_pikkus.grid(column=1,row=0)

root.mainloop()
