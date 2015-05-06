##from Tkinter import *
##
##master = Tk()
##
##w = Canvas(master, width=200, height=100)
##w.pack()
##
##w.create_line(0, 0, 200, 100)
##w.create_line(200, 0, 0, 100, fill="red", dash=(4, 4))
##
##w.create_rectangle(50, 25, 150, 75, fill="blue")
##
##mainloop()
from Tkinter import *
from numpy import *
import Tkinter as tk

scale=1

class Demonstrator:

   def __init__(self, master=None): 
      global full_coordinates, dimensions, scale
      self.master=master
      self.master.title( "Demonstrator 2")
      self.master.grid()
      self.master.rowconfigure(0, weight=1)
      self.master.columnconfigure(0, weight=1)

      self.canvas = Canvas(self.master, width=300, height=300, bg='grey')
      self.canvas.grid(row=0, rowspan=3, column=0)
      self.canvas.create_rectangle(full_coordinates[0],dimensions[0], activefill='blue', fill='red')
      self.canvas.create_rectangle(full_coordinates[1],dimensions[1], activefill='blue', fill='red')
      self.canvas.create_line(full_coordinates[0],full_coordinates[1], fill='red')

      a=9*scale
      Originx=10
      Originy=35
      coordinates1=[]
      coordinates2=[]

      x,y,i=Originx,Originy,1
      x1,y1,i=Originx,Originy,1

      while len(coordinates1)<=25:
       coordinates1.append((x,y))
       coordinates2.append((x1,y1))

       i+=1
       if i % 2 == 0:
            x,y=x+a,y
            x1,y1=x1,y1+a
       else:
            x,y=x,y+a
            x1,y1=x1+a,y1

       full_coordinates=list(set(coordinates1+coordinates2))
       b=array(full_coordinates)
       k=b+10
       dimensions=k.tolist()

class Settings:
    def __init__(self, parent):

        top = self.top = tk.Toplevel(parent)
        self.top.title('Settings')

        self.spinbox_Label= tk.Label(top, text='Change Scale Factor?')
        self.spinbox_Label.grid(row=0, column=0, columnspan=2)

        self.spinbox_Label= tk.Label(top, width=30, text='Scale factor:')
        self.spinbox_Label.grid(row=1, column=0)

        self.spinbox= tk.Spinbox(top, from_=1, to=10, increment=0.1, command=self.change)
        self.spinbox.grid(row=1, column=1)


    def change(self):
        global scale
        scale=float(self.spinbox.get())
        MG=Demonstrator(root) #This just generates a new Demonstrator with original coordinates

def onClick():
    inputDialog = Settings(root)
    root.wait_window(inputDialog.top)

def onClick2():
    print scale

class coords:
    global full_coordinates, dimensions, scale
    print scale
    a=9*scale
    Originx=10
    Originy=35
    coordinates1=[]
    coordinates2=[]

    x,y,i=Originx,Originy,1
    x1,y1,i=Originx,Originy,1

    while len(coordinates1)<=25:
       coordinates1.append((x,y))
       coordinates2.append((x1,y1))

       i+=1
       if i % 2 == 0:
            x,y=x+a,y
            x1,y1=x1,y1+a
       else:
            x,y=x,y+a
            x1,y1=x1+a,y1

       full_coordinates=list(set(coordinates1+coordinates2))
       b=array(full_coordinates)
       k=b+10
       dimensions=k.tolist()    




root=Tk()
root.minsize=(700,700)
root.geometry=('600x600')
MG=Demonstrator(root)
mainButton2 = tk.Button(root, width=20, text='Print "scale"', command=onClick2)
mainButton2.grid(row=1, column=1)
mainButton = tk.Button(root, width=20, text='Settings', command=onClick)
mainButton.grid(row=2, column=1)
root.mainloop()
mainButton2.grid(row=1, column=1)
mainButton = tk.Button(root, width=20, text='Settings', command=onClick)
mainButton.grid(row=2, column=1)
root.mainloop()
