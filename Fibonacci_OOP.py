from Fibonacci import fibonacci
from time import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from nuppudega_oo_konn import KonnaRakendus

class FibonacciFrame(Frame):

    def __init__(self, parent):
        #Kutsume valja ylemklassi __init__ meetodit
        super().__init__(parent)
        # tekitame sisendi muutuja ja valikukasti
        self.n_var = IntVar()
        arvud20ni = list(range(1,100))
        n_combo = Combobox(self, textvariable=self.n_var, values = arvud20ni)
        n_combo.grid(row=0,column=0)
        n_combo.bind('<<ComboboxSelected>>', self.arvuta_fibo)

        #Tekitame valjundi muutuja ja tekstikasti
        self.fibo_var = IntVar()
        fibo_entry = Entry(self, textvariable = self.fibo_var)
        fibo_entry.grid(row=0,column=1)
        
    def arvuta_fibo(self,event):
        #print(event.__dict__)
        vastus = fibonacci(self.n_var.get())
        self.fibo_var.set(vastus)

def about():

    messagebox.showinfo(title="About", message="Fibbonacci jada arvutamise rakenduse versioon 0.1")

def help_us():
    messagebox.showinfo(title="Help", message="Valige vasakust kastist arv ja vaadake valjundit")

    
    
if __name__ == '__main__':
    def frog_window():
        global root
        uus_aken = Toplevel(root)
        uus_aken.rowconfigure(0,weight=1)
        uus_aken.columnconfigure(0,weight=1)
        kr = KonnaRakendus(uus_aken)
        kr.grid(row=0,column=0,sticky=(N,S,W,E))
        
    root = Tk()
    minu_rakendus = FibonacciFrame(root)
    #Tekitame rakensulele menyy
    menubar= Menu(root)
    menubar.add_command(label='Frog', command=frog_window)
    info_submenu = Menu(menubar)
    info_submenu.add_command(label='Help', command=help_us)
    info_submenu.add_command(label='About',command=about)
    menubar.add_cascade(menu = info_submenu, label="Info")
    root.config(menu=menubar)

    #Paigutame minu_rakendus  Frame'i
    minu_rakendus.grid(row=0,column=0)
    root.mainloop()
