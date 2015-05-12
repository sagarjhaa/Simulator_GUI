import Tkinter as tk

class Settings:
    def __init__(self, parent):

        top = self.top = tk.Toplevel(parent)
        self.top.title('Settings')

        #Node Control
        self.spinbox_Label= tk.Label(top, text='Number of Nodes?')
        self.spinbox_Label.grid(row=0, column=0)

        self.spinbox_Label= tk.Label(top,text='Nodes:')
        self.spinbox_Label.grid(row=1, column=0)

        self.No_Nodes_Scale = tk.Scale(top,from_=2, to=200,length=200)#orient=HORIZONTAL,
        self.No_Nodes_Scale.set(5)
        self.No_Nodes_Scale.bind("<ButtonRelease-1>",self.change)#,self.update_beta_2
        self.No_Nodes_Scale.grid(row=1,column=1)
    
    def change(self,event):
        global scale
        scale = event.widget.get()
        return scale
        #print scale
        #MG=Network(root) #This just generates a new Network with original coordinates
