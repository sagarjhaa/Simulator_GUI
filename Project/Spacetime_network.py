from Tkinter import *
import Tkinter as tk
import random as rd

from Community_Coordinates import CommunityCoordinates_Generator
#from diffusion.SimulatorExperimence import SimulatorExperimence
from diffuse.Simulator import Simulator

Communities = 4
n1 = 5
n2 = 5
n3 = 5
n4 = 5
Radius = 10

class Network:

    def __init__(self,master=None):

        self.master = master
        self.master.title("Network Simulator")
        self.master.grid()
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.canvas = Canvas(self.master,width=w,height=h,bg="grey")
        self.canvas.grid(row=0,rowspan=1,column=0)
        
        self.Community_Coordinate = {}
        self.Communities = Communities
        self.Community_Coordinate = CommunityCoordinates_Generator(self.Communities,w,h)
        
        #print self.Community_Coordinate
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

        self.Radius = Radius
        self.Half_Radius = Radius/2
        
        for i in range(1,self.Communities+1):
            _polygon = self.canvas.create_polygon(self.Community_Coordinate[i][0],outline='red',width=2) #fill='#d47284'
            
            if i == 1:
                self.canvas.itemconfig(_polygon,fill="#d47284")

                s = Simulator(self.n1)
                Point_List=[]
                s.genPoints(self.Community_Coordinate[1])
                s.genLinks(self.n1*10)
                Point_List=s.pAll
                
                for jNode in range(len(Point_List)):
                    #print jNode,s.pAll[jNode].links,len(s.pAll[jNode].links)
                    #print j,s.pAll[j].links[0]
                    print len(s.pAll[jNode].links),0.2*10*self.n1
                    if len(s.pAll[jNode].links) <= 0.1*10*self.n1:
                        _oval = self.canvas.create_oval(Point_List[jNode].x,Point_List[jNode].y, Point_List[jNode].x + self.Radius, Point_List[jNode].y + self.Radius, outline="black",fill="green", width=2,activefill="green")
                    else:
                        _oval = self.canvas.create_oval(Point_List[jNode].x,Point_List[jNode].y, Point_List[jNode].x + self.Radius, Point_List[jNode].y + self.Radius, outline="black",width=2,activefill="green")
                    for iNode in range(len(s.pAll[jNode].links)):
                        a= s.pAll[jNode].links[iNode]
                        self.canvas.create_line(Point_List[jNode].x + self.Half_Radius,Point_List[jNode].y + self.Half_Radius, Point_List[a].x + self.Half_Radius,Point_List[a].y + self.Half_Radius,fill="blue", dash=(4, 4),tags = i)

            if i ==2:
                self.canvas.itemconfig(_polygon,fill="#b0ff01")

                s = Simulator(self.n2)
                Point_List=[]
                s.genPoints(self.Community_Coordinate[i])
                Point_List=s.pAll

                for j in range(len(Point_List)):
                    _oval = self.canvas.create_oval(Point_List[j].x,Point_List[j].y, Point_List[j].x+10, Point_List[j].y+10, outline="black", width=2,activefill="green")
                
            if i ==3:
                self.canvas.itemconfig(_polygon,fill="#4d1b7b")

                s = Simulator(self.n3)
                Point_List=[]
                s.genPoints(self.Community_Coordinate[i])
                Point_List=s.pAll

                for j in range(len(Point_List)):
                    _oval = self.canvas.create_oval(Point_List[j].x,Point_List[j].y, Point_List[j].x+10, Point_List[j].y+10, outline="black", width=2,activefill="green")
                    
            if i ==4:
                self.canvas.itemconfig(_polygon,fill="#3279d3")

                s = Simulator(self.n4)
                Point_List=[]
                s.genPoints(self.Community_Coordinate[i])
                Point_List=s.pAll

                for j in range(len(Point_List)):
                    _oval = self.canvas.create_oval(Point_List[j].x,Point_List[j].y, Point_List[j].x+10, Point_List[j].y+10, outline="black", width=2,activefill="green")
                    
            #print _polygon

##        Point_List=[]
##        Point_List = self.__simulate()
##        for i in range(len(Point_List)):
##            _oval = self.canvas.create_oval(Point_List[i].x,Point_List[i].y, Point_List[i].x+10, Point_List[i].y+10, outline="black", width=2,activefill="green")
        
##        XmaxNo = max(self.Community_Coordinate[1][1])
##        XminNo = min(self.Community_Coordinate[1][1])
##        YmaxNo = max(self.Community_Coordinate[1][2])
##        YminNo = min(self.Community_Coordinate[1][2])
##        self.Nodes = {}
##        self.Links = {}
##        
##        radius = 20
##        half_radius = radius/2
##        
##        for i in range(scale):
##            inside = False
##            while not inside:
##                x = rd.randrange(XminNo+1,XmaxNo-radius)
##                y = rd.randrange(YminNo+1,YmaxNo-radius)
##                inside = point_inside_polygon(x,y,self.Community_Coordinate[1][0])
##               
##            _oval = self.canvas.create_oval(x,y, x+radius, y+radius, outline="black", width=2,activefill="green")
##            #print _oval
##            self.canvas.tag_bind(_oval,'<ButtonPress-1>',self.__showLinkInfo)
##            self.Nodes[_oval] = [x,y]
##            self.Links[_oval] = []
##
##            if i==0:
##                tempid = _oval
##            if i==1:
##                #self.Links[_oval].append(0)
##                self.Links[tempid].append(_oval)
##                self.canvas.create_line(x+half_radius, y+half_radius, self.Nodes[tempid][0]+half_radius, self.Nodes[tempid][1]+half_radius,fill="blue", dash=(4, 4),tags = i)
##            if i>1:
##                j = rd.choice(self.Nodes.keys())
##                while j == _oval:
##                    j = rd.choice(self.Nodes.keys())
##                #self.Links[_oval].append(j)
##                self.Links[j].append(_oval) #added
##                self.canvas.create_line(x+half_radius, y+half_radius, self.Nodes[j][0]+half_radius, self.Nodes[j][1]+half_radius,fill="white", dash=(4, 4),tags = i)
##        #print self.Links

##    def __simulate(self):
##        """
##        This function will create object of SimulatorExperimence 
##        """
##        self.Sim = SimulatorExperimence()
##        ## Test to check object type       
##        ## print(type(self.Sim))
##        return self.Sim.doT1nT2n(self.Community_Coordinate)
                
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
            Nodes_Id = self.Nodes.keys()
            for i in range(len(Nodes_Id)):
                self.canvas.itemconfig(Nodes_Id[i],fill="")
                
            try:
                if len(self.Links[widget_id[0]]) > 0:
                    for i in range(len(self.Links[widget_id[0]])):
                        print self.nodeConverter(self.Links[widget_id[0]][i]),"--->",pNode
                        self.canvas.itemconfig(self.Links[widget_id[0]][i],fill="red")
            except:
                pass
        
class Settings:
    def __init__(self, parent):

        top = self.top = tk.Toplevel(parent)
        self.top.title('Settings')

        #Community Control
        self.spinbox_Label= tk.Label(top, text='Number of Community?')
        self.spinbox_Label.grid(row=0, column=0)

        self.spinbox_Label= tk.Label(top,text='Community:')
        self.spinbox_Label.grid(row=1, column=0)

        self.No_Nodes_Scale = tk.Scale(top,from_=1, to=4,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale.set(4)
        self.No_Nodes_Scale.bind("<ButtonRelease-1>",self.changeCommunities)#,self.update_beta_2
        self.No_Nodes_Scale.grid(row=1,column=1)

        #Node Control - 1
        self.spinbox_Label= tk.Label(top, text='Number of Nodes?')
        self.spinbox_Label.grid(row=2, column=0)

        self.spinbox_Label= tk.Label(top,text='Nodes 1:')
        self.spinbox_Label.grid(row=3, column=0)

        self.No_Nodes_Scale1 = tk.Scale(top,from_=2, to=200,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale1.set(5)
        self.No_Nodes_Scale1.bind("<ButtonRelease-1>",self.changeNodes_n1)#,self.update_beta_2
        self.No_Nodes_Scale1.grid(row=3,column=1)

        #Node Control - 2
        self.spinbox_Label= tk.Label(top, text='Number of Nodes?')
        self.spinbox_Label.grid(row=4, column=0)

        self.spinbox_Label= tk.Label(top,text='Nodes 2:')
        self.spinbox_Label.grid(row=5, column=0)

        self.No_Nodes_Scale2 = tk.Scale(top,from_=2, to=200,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale2.set(5)
        self.No_Nodes_Scale2.bind("<ButtonRelease-1>",self.changeNodes_n2)#,self.update_beta_2
        self.No_Nodes_Scale2.grid(row=5,column=1)

        #Node Control - 3
        self.spinbox_Label= tk.Label(top, text='Number of Nodes?')
        self.spinbox_Label.grid(row=6, column=0)

        self.spinbox_Label= tk.Label(top,text='Nodes 3:')
        self.spinbox_Label.grid(row=7, column=0)

        self.No_Nodes_Scale2 = tk.Scale(top,from_=2, to=200,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale2.set(5)
        self.No_Nodes_Scale2.bind("<ButtonRelease-1>",self.changeNodes_n3)#,self.update_beta_2
        self.No_Nodes_Scale2.grid(row=7,column=1)

        #Node Control - 4
        self.spinbox_Label= tk.Label(top, text='Number of Nodes?')
        self.spinbox_Label.grid(row=8, column=0)

        self.spinbox_Label= tk.Label(top,text='Nodes 4:')
        self.spinbox_Label.grid(row=9, column=0)

        self.No_Nodes_Scale2 = tk.Scale(top,from_=2, to=200,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale2.set(5)
        self.No_Nodes_Scale2.bind("<ButtonRelease-1>",self.changeNodes_n4)#,self.update_beta_2
        self.No_Nodes_Scale2.grid(row=9,column=1)

        #Radius Control
        self.spinbox_Label= tk.Label(top, text='Radius of Nodes?')
        self.spinbox_Label.grid(row=10, column=0)

        self.spinbox_Label= tk.Label(top,text='Radius:')
        self.spinbox_Label.grid(row=11, column=0)

        self.No_Nodes_Scale2 = tk.Scale(top,from_=2, to=20,orient=HORIZONTAL,length=200)
        self.No_Nodes_Scale2.set(10)
        self.No_Nodes_Scale2.bind("<ButtonRelease-1>",self.changeRadius)#,self.update_beta_2
        self.No_Nodes_Scale2.grid(row=11,column=1)


    def changeCommunities(self,event):
        global Communities
        Communities = event.widget.get()
        MG=Network(root) #This just generates a new Network with original coordinates
    
    def changeNodes_n1(self,event):
        global n1
        n1 = event.widget.get()
        #print scale
        MG=Network(root) #This just generates a new Network with original coordinates

    def changeNodes_n2(self,event):
        global n2
        n2 = event.widget.get()
        #print scale
        MG=Network(root) #This just generates a new Network with original coordinates
        
    def changeNodes_n3(self,event):
        global n3
        n3 = event.widget.get()
        #print scale
        MG=Network(root) #This just generates a new Network with original coordinates

    def changeNodes_n4(self,event):
        global n4
        n4 = event.widget.get()
        #print scale
        MG=Network(root) #This just generates a new Network with original coordinates

    def changeRadius(self,event):
        global Radius
        Radius = event.widget.get()
        MG = Network(root)
        
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
#root.minsize=(1000,900)
#root.attributes('-fullscreen',True)  #It will hide the title bar but open in maximized mode
w,h = root.winfo_screenwidth(),root.winfo_screenheight()  #It gives screen widht and height
#root.geometry("%dx%d+0+0" % (w,h))

root.state('zoomed')
root.geometry=("1000x900+0+0")

MG=Network(root)
mainButton = tk.Button(root, width=20, text='Settings',command=onClick)
mainButton.grid(row=1, column=1)
##mainButton = tk.Button(root, width=20, text='Opinion Leader',command=onClick2)
##mainButton.grid(row=2, column=1)
root.mainloop()
