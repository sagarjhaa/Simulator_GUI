'''
Created on 2013-5-20

@author: guyil
'''
from Tkinter import *

class MainCanvas(object):
    '''
    Create canvas and draw polygons in different color
    '''


    def __init__(self,COUNTYSET,root,attributeName,datalist,year_Predict):
        self.COUNTYSET = COUNTYSET
        self.root = root
        self.attributeName = attributeName
        self.datalist = datalist
        self.createCanvas(year_Predict)
        pass
    
    def createCanvas(self,year_Predict):
        self.canvasRoot = Toplevel()
        self.canvasRoot.title("Simulated for year "+str(year_Predict))
        self.canvasRoot.lower(belowThis = self.root)
        self.mainCanvas = Canvas(self.canvasRoot, bg = 'white', width = 600, height = 600, scrollregion=('-50c','-50c',"50c","50c") )
    
        self.drawPolygon()
        self.mainCanvas.pack()
    
    def drawPolygon(self):     
        tag_count=0
        for polygon in self.COUNTYSET:
            if len(polygon.Coordinate) == 1:
                
                _polygon=self.mainCanvas.create_polygon(polygon.Coordinate, fill = polygon.Color, outline='black',
                                               tags = self.datalist[tag_count] )
            
                self.mainCanvas.tag_bind( _polygon, '<ButtonPress-1>', self.callback)      
                
            else:
                #print "multiple!!"
                for sub_polygonCoordinate in polygon.Coordinate:
                    polygon=self.mainCanvas.create_polygon(sub_polygonCoordinate, fill = polygon.Color, outline='black',
                                                   tag = polygon.Color )
            
            tag_count+=1
            #print tag_count
        

    
    def callback(self,event):
        #print "click!!!!"
        #print event.widget.find_closest(event.x, event.y) 
        widget_id=event.widget.find_closest(event.x, event.y) 
        #print self.attributeName+" is: "+self.mainCanvas.gettags(widget_id)[0]
        '''
        Constructor
        '''
        
