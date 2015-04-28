'''
Created on 2013-5-20

@author: guyil
'''
from Tkinter import *
import ttk 
import tkFileDialog
import ArcView as ARCVIEW
from ArcView import ArcViewProject
from GIS_DataStructure import *
from MainCanvas import MainCanvas
from Problem_Solver import *
import Problem_Solver
from random import *


class MainMenu(object):
    '''
    classdocs
    '''
    # initiate all parameters  
    year_Predict=2013
    currentAttribute=""
    Compute_Step=1000
    # probability p of being born in obesogenic enviroment between 0.5 and  1
    p=0.55
    # birth rate between 0 and 0.05
    mu=0.0144
    # social influence by overweight and obeses between 0 and 0.5
    k_1=0.4
    k_2=0.2
    alpha=0.05
    a=0.14
    a_1=0.08
    a_2=0.014
    beta_2=0.05
    beta_3=0.03
    # rate of weight loss to each class: extremely obese to obese, obese to overweight, overweight to normal weight
    rho_1=0.033
    # rate of weight regainers transitioning from normal weight to overweight
    rhoR=0.04
    # death rate of obese and extremely obese population
    D_0=uniform(16.5,22.0)

    # the death rate D of susceptible, overweight and recovered
    # populations is lower than the death rate D0 for obese
    # and extremely obese populations
    D=0.0144

    # default model
    Module="dynamicModel"
    
    def __init__(self):
        self.POLYGONSET=[]
        self.root = Tk()
        self.root.minsize(670,600)
        self.root.maxsize(670,600)
        self.root.title('Simulation')
        
        self.createMenu()
        
        self.root.mainloop()
        

    def createMenu(self):   
        self.menubar = Menu(self.root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.openShpfile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)
        
##        self.attibmenu = Menu(self.menubar, tearoff=0)
##        self.menubar.add_cascade(label="Attribute", menu=self.attibmenu,state='disabled')

        self.attibmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Module", menu=self.attibmenu,state='disabled')
       
        self.root.config(menu=self.menubar)


        
    # create slider for user to input every parameter
    
    def createSlider(self):
        master = self.root
        Label(master, text='Year:').grid(column=4, row=5,sticky=W,pady=3)
        v=StringVar()
        year_Predict_Combobox = ttk.Combobox(master, textvar=v,state='readonly', values=['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023'])
        year_Predict_Combobox.current(0)
        year_Predict_Combobox.grid(column=5, row=5)
        year_Predict_Combobox.bind(' <<ComboboxSelected>>',self.update_year_Predict)
        
        Label(master,text='       ').grid(column=2, row=4,sticky=W,pady=3)
        Label(master,text='Parameters:').grid(column=3, row=6,sticky=W,pady=3)
        
        Pslider=Scale(master,from_=0.0, to=1.0,orient=HORIZONTAL,resolution=0.01,label='Prob. of born in obesogenic environ', length=200)
        Pslider.set(0.55)
        Pslider.bind("<ButtonRelease-1>", self.updateP)
        Pslider.grid(column=3, row=7,sticky=W,pady=3)

        D_0_Slider=Scale(master,from_=16.5, to=22.0,orient=HORIZONTAL,resolution=0.5, label='Death rate: obese and extreme obese',length=200)
        Pslider.set(16.5)
        D_0_Slider.bind("<ButtonRelease-1>", self.update_D_0)
        D_0_Slider.grid(column=3, row=8,sticky=W,pady=3)
        
        beta_2_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01, label='Rate of extremely obese to obese', length=200)
        beta_2_Slider.set(0.05)
        beta_2_Slider.bind("<ButtonRelease-1>", self.update_beta_2)
        beta_2_Slider.grid(column=3, row=9,sticky=W,pady=3)

        #add
        k_1_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01, label='Social influence: overweight',length=200)
        k_1_Slider.bind("<ButtonRelease-1>", self.update_k_1)
        k_1_Slider.set(0.4)
        k_1_Slider.grid(column=3, row=10,sticky=W,pady=3)

        k_2_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01,label='Social influence: obese',length=200)
        beta_2_Slider.set(0.2)
        k_2_Slider.bind("<ButtonRelease-1>", self.update_k_2)
        k_2_Slider.grid(column=3, row=11,sticky=W,pady=3)

        alpha_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01,label='Rate of weight gain: exposed',length=200)
        alpha_Slider.set(0.05)
        alpha_Slider.bind("<ButtonRelease-1>", self.update_alpha)
        alpha_Slider.grid(column=3, row=12,sticky=W,pady=3)

    

        ###########
                
        rho_1_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01, label='Rate of overweight to normal',length=200)
        rho_1_Slider.set(0.033)
        rho_1_Slider.bind("<ButtonRelease-1>", self.update_rho_1)
        rho_1_Slider.grid(column=6, row=7,sticky=W,pady=3)

        rhoR_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01, label='Rate of normal to overweight', length=200)
        rhoR_Slider.set(0.04)
        rhoR_Slider.bind("<ButtonRelease-1>", self.update_rhoR)
        rhoR_Slider.grid(column=6, row=8,sticky=W,pady=3)

        beta_3_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01, label='Rate of obese to overweight', length=200)
        beta_3_Slider.set(0.03)
        beta_3_Slider.bind("<ButtonRelease-1>", self.update_beta_3)
        beta_3_Slider.grid(column=6, row=9,sticky=W,pady=3)
        
        #add
        a_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01,label='Rate of weight gain: overweight',length=200)
        a_Slider.set(0.14)
        a_Slider.bind("<ButtonRelease-1>", self.update_a)
        a_Slider.grid(column=6, row=10,sticky=W,pady=3)
        
        a_1_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01,label='Rate of weight gain: obese',length=200)
        a_1_Slider.set(0.08)
        a_1_Slider.bind("<ButtonRelease-1>", self.update_a_1)
        a_1_Slider.grid(column=6, row=11,sticky=W,pady=3)

        
        a_2_Slider=Scale(master,from_=0, to=0.5,orient=HORIZONTAL,resolution=0.01,label='Rate of weight gain: extremely obese',length=200)
        a_2_Slider.set(0.014)
        a_2_Slider.bind("<ButtonRelease-1>", self.update_a_2)
        a_2_Slider.grid(column=6, row=12,sticky=W,pady=3)


        ## add birthrate and deathrate textbox
        Label(master, text='Birth rate:').grid(column=3, row=13,sticky=W,pady=3)
        Birthrate_Entry=Entry(master)
        Birthrate_Entry.insert(0, '0.0144')
        Birthrate_Entry.bind("<KeyRelease>",self.update_mu)
        
        Birthrate_Entry.grid(column=3, row=14,sticky=W,pady=3)

        Label(master, text='Death rate:').grid(column=6, row=13,sticky=W,pady=3)
        Deathrate_Entry=Entry(master)
        Deathrate_Entry.insert(0, '0.0144')
        Deathrate_Entry.bind("<KeyRelease>",self.updateD)
        Deathrate_Entry.grid(column=6, row=14,sticky=W,pady=3)
        
        confirmButton=Button(master,text="Update",command=self.executeUpdate)
        confirmButton.grid(column=5, row=16,sticky=W,pady=3) 

    ## update all parameters 
    def update_year_Predict(self, event):
        self.year_Predict=event.widget.get()
    def updateP(self,event):
        self.P=event.widget.get()
    def update_mu(self,event):
        value=event.widget.get()
        if value=="":
            self.mu=0.0144
        else:
            self.mu=float(value)
    def update_k_1(self,event):
        self.k_1=event.widget.get()
    def update_k_2(self,event):
        self.k_2=event.widget.get()
    def update_alpha(self,event):
        self.alpha=event.widget.get()
    def update_a(self,event):
        self.a=event.widget.get()
    def update_a_1(self,event):
        self.a_1=event.widget.get()
    def update_a_2(self,event):
        self.a_2=event.widget.get()
    def update_beta_2(self,event):
        self.beta_2=event.widget.get()
    def update_beta_3(self,event):
        self.beta_3=event.widget.get()
    def update_rho_1(self,event):
        self.rho_1=event.widget.get()
    def update_rhoR(self,event):
        self.rhoR=event.widget.get()
    def update_D_0(self,event):
        self.D_0=event.widget.get()
    def updateD(self,event):
        value=event.widget.get()
        if value=="":
            self.D=0.0144
        else:
            self.D=float(value)


    def executeUpdate(self):
        self.updateColor(self.canvas)
  
    def openShpfile(self):
        import Projection
        import CanvasCoords

        #print "open shapefile!"
        directory=tkFileDialog.askopenfilename(filetypes=[("SHAPE_FILE","*.shp")])
        #print directory
        
        #read shape file data
        try:
            reader = open(directory, 'rb')
            shpread = reader.read(100)      # first 100 bytes contain header
        except:
            return    

        
        map = Projection.Map(directory, 0)  
        C = CanvasCoords.CanvasCoords()
        C.set_coordinate_system(600, 600, 300, 300, map.xrange)
        p2c2 = C.physical2canvas2
        index = 0
        ##print len(map.projected.keys())
        self.shape2poly=map.shape2poly 
        ##print self.shape2poly
        for key in map.projected.keys():
            polygon = map.projected[key]
            pnts = [p2c2(point) for point in polygon]
            output = [pnts]
            county = County(output)
            self.POLYGONSET.append(county)
            index += 1

              
        #read corresponding dbf data
        dbfFile = directory[:-4]
        dbfFile += ".dbf"
        arc = ARCVIEW.ArcViewProject(dbfFile)
        arc.summary()
        arc.table2variables()
        self.dbfdata = arc.variables
        #add attributes into menu
##        for key in self.dbfdata.keys():  
##            self.addAttributes(key)

        
        self.addModules("dynamic model")
        self.menubar.entryconfig(2, state=NORMAL)
        self.updateCanvas('S_T')
        self.createSlider()
        #self.openCanvas
    
    def addAttributes(self,attributeName):
        self.attibmenu.add_command(label=attributeName, command=lambda i=attributeName:self.updateCanvas(i))
        pass
    def addModules(self,moduleName):
        self.attibmenu.add_command(label=moduleName, command=lambda i=moduleName:self.updateModel(i))
        pass

    def updateModel(self, modelName):
        self.Module=modelName
    
    
    def openCanvas(self):
        
        self.canvas=MainCanvas(self.POLYGONSET,self.root)
       
        pass
    
    def updateCanvas(self, attributeName):
        
        #print "update Canvas "+attributeName
        self.currentAttribute=attributeName

        Sdatalist=self.dbfdata['S_T']
        Sdatalist=[float(i) for i in Sdatalist]
        ETPdatalist=self.dbfdata['ETP']
        ETPdatalist=[float(i) for i in ETPdatalist]
        ETNdatalist=self.dbfdata['ETN']
        ETNdatalist=[float(i) for i in ETNdatalist]
        RTPdatalist=self.dbfdata['RTP']
        RTPdatalist=[float(i) for i in RTPdatalist]
        RTNdatalist=self.dbfdata['RTN']
        RTNdatalist=[float(i) for i in RTNdatalist]
        
        Edatalist=[float(i)* float(j) for i, j in zip(ETPdatalist, ETNdatalist)]
        Rdatalist=[float(i)* float(j) for i, j in zip(RTPdatalist, RTNdatalist)]
    
        I_1_datalist=self.dbfdata['1_T']
        I_1_datalist=[float(i) for i in I_1_datalist]
        I_1_datalist=self.dbfdata['1_T']
        I_1_datalist=[float(i) for i in I_1_datalist]
        I_2_datalist=self.dbfdata['2_T']
        I_2_datalist=[float(i) for i in I_2_datalist]
        I_3_datalist=self.dbfdata['2_T']
        I_3_datalist=[float(i) for i in I_3_datalist]

        datalist=self.dbfdata[attributeName]
        data_poly=[]
        datalist=[float(i) for i in datalist]
        count=0
        for i in range(len(datalist)):
            initialSum=Sdatalist[i]+Edatalist[i]+I_1_datalist[i]+I_2_datalist[i]+I_3_datalist[i]
            initialRatio=datalist[i]/initialSum
            #print initialRatio
            data_poly.append(initialRatio)
            for item in self.shape2poly[i]:
                if initialRatio<0.20:
                    self.POLYGONSET[count].Color="red"
                elif initialRatio>=0.20 and initialRatio<0.30:
                    self.POLYGONSET[count].Color="pink"
                elif initialRatio>=0.30 and initialRatio<0.40:
                    self.POLYGONSET[count].Color="white"
                elif initialRatio>=0.40 and initialRatio<0.50:
                    self.POLYGONSET[count].Color="green"
                elif initialRatio>=0.50:
                    self.POLYGONSET[count].Color="blue" 
                data_poly.append(datalist[i])
                count+=1
            
        #print count, i         
        self.canvas=MainCanvas(self.POLYGONSET,self.root,attributeName,data_poly,self.year_Predict)
        self.root1=Tk();
        self.root1.minsize(175,150)
        self.root1.maxsize(175,150)
        self.root1.title('Legend')
        Label(self.root1,text='      ').grid(column=1, row=4,sticky=W,pady=3)
        Label(self.root1,bg="red",width=3).grid(column=4, row=2,sticky=W,pady=3)
        Label(self.root1,text=' < 20%').grid(column=6, row=2,sticky=W,pady=3)
        Label(self.root1,bg="pink",width=3).grid(column=4, row=3,sticky=W,pady=3)
        Label(self.root1,text='20%~30%').grid(column=6, row=3,sticky=W,pady=3)
        Label(self.root1,bg="white",width=3).grid(column=4, row=4,sticky=W,pady=3)
        Label(self.root1,text='30%~40%').grid(column=6, row=4,sticky=W,pady=3)
        Label(self.root1,bg="green",width=3).grid(column=4, row=5,sticky=W,pady=3)
        Label(self.root1,text='40%~50%').grid(column=6, row=5,sticky=W,pady=3)
        Label(self.root1,bg="blue",width=3).grid(column=4, row=6,sticky=W,pady=3)
        Label(self.root1,text='>50%').grid(column=6, row=6,sticky=W,pady=3)

    #update polygonset
    def updateColor(self,canvas):
        Sdatalist=self.dbfdata['S_T']
        Sdatalist=[float(i) for i in Sdatalist]
        ETPdatalist=self.dbfdata['ETP']
        ETPdatalist=[float(i) for i in ETPdatalist]
        ETNdatalist=self.dbfdata['ETN']
        ETNdatalist=[float(i) for i in ETNdatalist]
        RTPdatalist=self.dbfdata['RTP']
        RTPdatalist=[float(i) for i in RTPdatalist]
        RTNdatalist=self.dbfdata['RTN']
        RTNdatalist=[float(i) for i in RTNdatalist]
        
        Edatalist=[float(i)* float(j) for i, j in zip(ETPdatalist, ETNdatalist)]
        Rdatalist=[float(i)* float(j) for i, j in zip(RTPdatalist, RTNdatalist)]
    
        I_1_datalist=self.dbfdata['1_T']
        I_1_datalist=[float(i) for i in I_1_datalist]
        I_1_datalist=self.dbfdata['1_T']
        I_1_datalist=[float(i) for i in I_1_datalist]
        I_2_datalist=self.dbfdata['2_T']
        I_2_datalist=[float(i) for i in I_2_datalist]
        I_3_datalist=self.dbfdata['2_T']
        I_3_datalist=[float(i) for i in I_3_datalist]
##        
        num_Years=int(self.year_Predict)-2013
        paraListName=['year_Predict', 'Compute_Step','p','mu','k_1','k_2','alpha','a','a_1','a_2','beta_2','beta_3','rho_1','rhoR','D_0','D']
        paraList=[self.year_Predict,self.Compute_Step,self.p, self.mu, self.k_1, self.k_2, self.alpha, self.a, self.a_1,self.a_2,self.beta_2,self.beta_3,self.rho_1,self.rhoR,self.D_0,self.D]
        ## wirte the updated parameters and predictions results into a corresponding txt file 
        fd = open(str(self.year_Predict)+" Updated Results.txt","w")
        print >> fd, paraListName
        print >> fd, paraList
        predictListName=['ploygonID','S','E','I_1','I_2','I_3','R','SUpdateRatio','IncreaseRate']
        print >> fd, predictListName
        count=0
        IncreaseRateUpdateList=[]
        ploygonID=2
        for i in range(len(Sdatalist)):
            initialSum=Sdatalist[i]+Edatalist[i]+I_1_datalist[i]+I_2_datalist[i]+I_3_datalist[i]
            SinitialRatio=Sdatalist[i]/initialSum            

            S,E,I_1,I_2,I_3,R=Problem_Solver.dynamicModel(num_Years,self.Compute_Step,self.p, self.mu, self.k_1, self.k_2, self.alpha, self.a, self.a_1,self.a_2,self.beta_2,self.beta_3,self.rho_1,self.rhoR,self.D_0,self.D,Sdatalist[i],Edatalist[i],I_1_datalist[i], I_2_datalist[i], I_3_datalist[i], Rdatalist[i])
            
            UpdataSum=S+E+I_1+I_2+I_3
            SUpdateRatio=S/UpdataSum
            IncreaseRate=(SUpdateRatio-SinitialRatio)/SinitialRatio
            #print InitialRation, UpdateRation
            IncreaseRateUpdateList.append(IncreaseRate)
            #print IncreaseRate
            
            print >> fd, ploygonID, S,E,I_1,I_2,I_3,R,SUpdateRatio,IncreaseRate
            for item in self.shape2poly[i]:
                if IncreaseRate<-0.15:
                    self.POLYGONSET[count].Color="red"
                elif IncreaseRate>=-0.15 and IncreaseRate<-0.05:
                    self.POLYGONSET[count].Color="pink"
                elif IncreaseRate>=-0.05 and IncreaseRate<0.05:
                    self.POLYGONSET[count].Color="white"
                elif IncreaseRate>=0.05 and IncreaseRate<0.15:
                    self.POLYGONSET[count].Color="cyan"
                elif IncreaseRate>=0.15:
                    self.POLYGONSET[count].Color="blue" 
                count+=1
            ploygonID+=1
        fd.close()
        self.canvas=MainCanvas(self.POLYGONSET,self.root,canvas.attributeName,IncreaseRateUpdateList,self.year_Predict)
        self.root=Tk();
        self.root.minsize(175,150)
        self.root.maxsize(175,150)
        self.root.title('Legend')
        Label(self.root,text='      ').grid(column=1, row=4,sticky=W,pady=3)
        
        Label(self.root,bg="red",width=3).grid(column=2, row=2,sticky=W,pady=3)
        Label(self.root,text=' < -15%').grid(column=4, row=2,sticky=W,pady=3)
        Label(self.root,bg="pink",width=3).grid(column=2, row=3,sticky=W,pady=3)
        Label(self.root,text='-15%~-5%').grid(column=4, row=3,sticky=W,pady=3)
        Label(self.root,bg="white",width=3).grid(column=2, row=4,sticky=W,pady=3)
        Label(self.root,text='-5%~5%').grid(column=4, row=4,sticky=W,pady=3)
        Label(self.root,bg="cyan",width=3).grid(column=2, row=5,sticky=W,pady=3)
        Label(self.root,text='5%~15%').grid(column=4, row=5,sticky=W,pady=3)
        Label(self.root,bg="blue",width=3).grid(column=2, row=6,sticky=W,pady=3)
        Label(self.root,text='>15%').grid(column=4, row=6,sticky=W,pady=3)


        
                  
if __name__ == '__main__':
    MainMenu=MainMenu()
    
    
