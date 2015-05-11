from Tkinter import *
import Tkinter as tk
import random as rd

scale = 5
poly = [10,10,990,10,990,590,10,590]
tempXlist = [10,990,990,10]
tempYlist = [10,10,590,590]

#poly = [456, 124, 446, 50, 483, 51, 483, 65, 499, 65, 524, 66, 526, 123, 514, 123, 513, 160, 485, 159, 460, 158, 459, 146, 457, 134, 456, 126, 456, 124]
#tempXlist = [456,446,483,483,499,524,526,514,513,485,460,459,457,456,456]
#tempYlist = [124,50,51,65,65,66,123,123,160,159,158,146,134,126,124]

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
        self.Nodes = {}
        self.Links = {}
        
        radius = 20
        half_radius = radius/2
        
        for i in range(scale):
            inside = False
            while not inside:
                x = rd.randrange(XminNo+1,XmaxNo-radius)
                y = rd.randrange(YminNo+1,YmaxNo-radius)
                inside = point_inside_polygon(x,y,poly)
            
            
            _oval = self.canvas.create_oval(x,y, x+radius, y+radius, outline="#f11", width=2,activefill="green")
            #print _oval
            self.canvas.tag_bind(_oval,'<ButtonPress-1>',self.__showLinkInfo)
            self.Nodes[_oval] = [x,y]
            self.Links[_oval] = []

            if i==0:
                tempid = _oval
            if i==1:
                #self.Links[_oval].append(0)
                self.Links[tempid].append(_oval)
                self.canvas.create_line(x+half_radius, y+half_radius, self.Nodes[tempid][0]+half_radius, self.Nodes[tempid][1]+half_radius,fill="red", dash=(4, 4),tags = i)
            if i>1:
                j = rd.choice(self.Nodes.keys())
                while j == _oval:
                    j = rd.choice(self.Nodes.keys())
                #self.Links[_oval].append(j)
                self.Links[j].append(_oval) #added
                self.canvas.create_line(x+half_radius, y+half_radius, self.Nodes[j][0]+half_radius, self.Nodes[j][1]+half_radius,fill="green", dash=(4, 4),tags = i)
        #print self.Links
        
                
    def nodeConverter(self,widget_id):

        if widget_id-1 ==1:
            #or widget_id-1 ==2:
            return widget_id-1
        else:
            tempnode = (widget_id/2)
            widget_id_1 = 2*tempnode - (tempnode -1)
            return widget_id_1

        
    def __showLinkInfo(self,event):
        widget_id = event.widget.find_closest(event.x,event.y)
        if widget_id[0]  <> 1:
            pNode = self.nodeConverter(widget_id[0])
            print "Node is:",pNode

            #self.canvas.itemconfig(widget_id[0],fill="red")   #important Line

            try:
                if len(self.Links[widget_id[0]]) > 0:
                    for i in range(len(self.Links[widget_id[0]])):
                        print self.nodeConverter(self.Links[widget_id[0]][i]),"--->",pNode
            except:
                pass
        
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
        #print scale
        MG=Network(root) #This just generates a new Network with original coordinates
        
def onClick():
    inputDialog = Settings(root)
    root.wait_window(inputDialog.top)

def onClick2():
    pass

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
##mainButton = tk.Button(root, width=20, text='Opinion Leader',command=onClick2)
##mainButton.grid(row=2, column=1)
root.mainloop()
