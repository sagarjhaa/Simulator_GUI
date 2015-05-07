from Tkinter import *
import Tkinter as tk
import random as rd

scale = 5
poly = [10,10,990,10,990,590,10,590]
tempXlist = [10,990,990,10]
tempYlist = [10,10,590,590]

class Network:

    def __init__(self,master=None):

        self.master = master
        self.master.title("Network Simulator")
        self.master.grid()
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.canvas = Canvas(self.master,width= 1000,height=600,bg="white")
        self.canvas.grid(row=0,rowspan=3,column=0)
        self.canvas.create_polygon(poly,outline='red',fill='black',width=2)

        

        XmaxNo = max(tempXlist)
        XminNo = min(tempXlist)
        YmaxNo = max(tempYlist)
        YminNo = min(tempYlist)
        PointList = {}
        radius = 20
        half_radius = radius/2
        
        for i in range(scale):
            inside = False
            while not inside:
                x = rd.randrange(XminNo+1,XmaxNo-radius)
                y = rd.randrange(YminNo+1,YmaxNo-radius)
                inside = point_inside_polygon(x,y,poly)
            PointList[i] = [x,y]
            
            self.canvas.create_oval(x,y, x+radius, y+radius, outline="#f11", width=2,activefill="green")
            if i==1:
                self.canvas.create_line(x+half_radius, y+half_radius, PointList[0][0]+half_radius, PointList[0][1]+half_radius,fill="red", dash=(4, 4))
            if i>1:
                j = rd.randrange(i)
                self.canvas.create_line(x+half_radius, y+half_radius, PointList[j][0]+half_radius, PointList[j][1]+half_radius,fill="green", dash=(4, 4))
         
class Settings:
    def __init__(self, parent):

        top = self.top = tk.Toplevel(parent)
        self.top.title('Settings')

        self.spinbox_Label= tk.Label(top, text='Number of Nodes?')
        self.spinbox_Label.grid(row=0, column=0)

        self.spinbox_Label= tk.Label(top,text='Nodes:')
        self.spinbox_Label.grid(row=1, column=0)

        self.No_Nodes_Scale = tk.Scale(top,from_=2, to=200,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale.set(5)
        self.No_Nodes_Scale.bind("<ButtonRelease-1>",self.change)#,self.update_beta_2
        self.No_Nodes_Scale.grid(row=1,column=1)
    
    def change(self,event):
        global scale
        scale = event.widget.get()
        print scale
        MG=Network(root) #This just generates a new Demonstrator with original coordinates
        
def onClick():
    inputDialog = Settings(root)
    root.wait_window(inputDialog.top)       

def point_inside_polygon(x,y,poly):
    n = len(poly)/2
    inside =False

    p1x = poly[0]
    p1y = poly[1]
    
    for i in range(0,n+1,1):
        p2x = poly [(i%n)*2]
        p2y = poly [(i%n)*2 +1]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

 
root=Tk()
root.minsize=(1000,900)
root.geometry=("1000x900+0+0")
MG=Network(root)
mainButton = tk.Button(root, width=20, text='Settings',command=onClick)
mainButton.grid(row=1, column=1)
root.mainloop()
