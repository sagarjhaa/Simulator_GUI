##from Tkinter import *
##
##master = Tk()
##
##w = Canvas(master, width=200, height=100)
##w.pack()
##
##w.create_line(0, 0, 200, 100)
##w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
##
##w.create_rectangle(50, 25, 150, 75, fill="blue")
##
##mainloop()

##i = w.create_line(xy, fill="red")
##
##w.coords(i, new_xy) # change coordinates
##w.itemconfig(i, fill="blue") # change color
##
##w.delete(i) # remove
##
##w.delete(ALL) # remove all items

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program draws three
rectangles filled with different
colors.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

##from Tkinter import Tk, Canvas, Frame, BOTH
##class Example(Frame):
##  
##    def __init__(self, parent):
##        Frame.__init__(self, parent)   
##         
##        self.parent = parent        
##        self.initUI()
##        
##    def initUI(self):
##      
##        self.parent.title("Colors")        
##        self.pack(fill=BOTH, expand=1)
##
##        canvas = Canvas(self)
##
##        canvas.create_rectangle(10, 25, 120, 80, 
##            outline="#fb0", fill="#F00")
##        canvas.create_oval(15, 50, 20, 55, outline="black", 
##            fill="green", width=2)
####        canvas.create_rectangle(150, 10, 240, 80, 
####            outline="#f50", fill="#f50")
####        canvas.create_rectangle(270, 10, 370, 80, 
####            outline="#05f", fill="#05f")            
##        canvas.pack(fill=BOTH, expand=1)
##
##
##def main():
##  
##    root = Tk()
##    ex = Example(root)
##    root.geometry("400x100+300+300")
##    root.mainloop()  
##
##
##if __name__ == '__main__':
##    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we draw basic 
shapes on the canvas.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

from Tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline="red", 
            fill="green", width=2)
        canvas.create_oval(110, 10, 210, 80, outline="#f11", 
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60, 
            outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 200, 90, 100, start=0, 
            extent=210, outline="#f11", fill="#1f1", width=2)
            
        points = [150, 100, 250, 100, 250, 180, 210, 
            200, 150, 150, 100, 200]
        abclist = [456, 124, 446, 50, 483, 51, 483, 65, 499, 65, 524, 66, 526, 123, 514, 123, 513, 160, 485, 159, 460, 158, 459, 146, 457, 134, 456, 126, 456, 124]
        canvas.create_polygon(abclist, outline='red',activefill="blue", 
            fill='black', width=2)
        
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()
