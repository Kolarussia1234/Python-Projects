import turtle
from tkinter import *
from tkinter.ttk import *  #Uuema valjanagemisega tkinter
from turtle import TurtleScreen,RawTurtle
root=Tk()

root.title('Kochi kõver nuppudega')
root.rowconfigure(index=0,weight=1)
root.columnconfigure(index=0,weight=1)
c = Canvas(root)
c.grid(column=0, row=0, sticky=(N, S, W, E))
ts = TurtleScreen(c)
ts.bgcolor('cyan')
turtle = RawTurtle(ts)
turtle.color('green')
turtle.penup()
turtle.setposition(0,-500)
turtle.pendown()




def koch():
    joonista_koch(pikkus.get(),min_pikkus.get())
    
def joonista_koch(pikkus,min_pikkus=1):
    if pikkus >= min_pikkus:

        turtle.speed(0)

        joonista_koch(pikkus/3,min_pikkus)
        
        turtle.left(60)

        joonista_koch(pikkus/3,min_pikkus)

        turtle.right(120)

        joonista_koch(pikkus/3,min_pikkus)

        turtle.left(60)
        
        joonista_koch(pikkus/3,min_pikkus)


    else:
        
         turtle.fd(pikkus)

f = Frame(root)
f.grid(column=0,row=1)


pikkus = IntVar()
pikkus.set(300)
lbl_pikkus = Label(root,text="    pikkus    ")
entry_pikkus=Entry(f,textvariable=pikkus)
entry_pikkus.grid(column=2,row=0)

min_pikkus = IntVar()
min_pikkus.set(100)
lbl_min_pikkus = Label(root,text="    min_pikkus    ")
entry_min_pikkus=Entry(f,textvariable=min_pikkus)
entry_min_pikkus.grid(column=3,row=0)



btn_Koch = Button(f,text="Kochi Kover",command=koch)
btn_Koch.grid(column=1,row=0)
        
root.mainloop()
