# L-9 MCS 275 Mon 30 Jan 2017 : koch.py

"""
A Koch curve fills up the gaps in the Cantor interval.
"""

from tkinter import Tk, IntVar, Scale, Button
from tkinter import Canvas, ALL
from math import sqrt

class KochCurve(object):
    """
    GUI to draw a Koch curve on canvas.
    """
    def __init__(self, wdw, N):
        """
        A Koch curve with N levels.
        """
        wdw.title('a Koch curve')
        self.dim = 3**N+20
        self.nvr = IntVar()
        self.scl = Scale(wdw, orient='horizontal', \
            from_=0, to=N, tickinterval=1, \
            length=self.dim, variable=self.nvr, \
            command=self.draw_curve)
        self.scl.set(0)
        self.scl.grid(row=0, column=0)
        self.cnv = Canvas(wdw, width=self.dim, \
            height=self.dim/3, bg='white')
        self.cnv.grid(row=1, column=0)
        self.btt = Button(wdw, text="clear canvas", \
            command=self.clear_canvas)
        self.btt.grid(row=2, column=0)

    def koch(self, left, right, k):
        """
        A Koch curve from left to right with k levels.
        """
        if k == 0:
            self.cnv.create_line(left[0], left[1], \
                right[0], right[1], width=2)
        else:
            nlf = ((2*left[0]+right[0])/3.0, (2*left[1]+right[1])/3.0)
            nrg = ((left[0]+2*right[0])/3.0, (left[1]+2*right[1])/3.0)
            mid = ((left[0]+right[0])/2.0, (left[1]+right[1])/2.0)
            ratio = sqrt(3)/6
            top = (ratio*(left[1]-right[1]), ratio*(right[0]-left[0]))
            peak = (mid[0]-top[0], mid[1]-top[1])
            self.koch(left, nlf, k-1)
            self.koch(nlf, peak, k-1)
            self.koch(peak, nrg, k-1)
            self.koch(nrg, right, k-1)

    def draw_curve(self, val):
        """
        Draws a Koch curve.
        """
        nbr = int(val)
        left = (10, self.dim/3-20)
        right = (self.dim-10, self.dim/3-20)
        self.koch(left, right, nbr)

    def clear_canvas(self):
        """
        Clears the entire canvas.
        """
        self.cnv.delete(ALL)

def main():
    """
    Instantiates the GUI object and
    launches the main event loop.
    """
    top = Tk()
    KochCurve(top, 6)
    top.mainloop()

if __name__ == "__main__":
    main()
