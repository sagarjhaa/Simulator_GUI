import random as rd
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

poly = [100,50,900,50,900,400,100,400]
tempXlist = [100,900,900,100]
tempYlist = [50,50,400,400]

XmaxNo = max(tempXlist)
XminNo = min(tempXlist)
YmaxNo = max(tempYlist)
YminNo = min(tempYlist)

inside = False

PointList = {}
from Tkinter import *
import random
master = Tk()

w = Canvas(master, width=1000, height=500)
w.pack()
w.create_polygon(poly, outline='red', fill='White', width=2)

for i in range(6):
    inside = False
    while not inside:
        x = rd.randrange(XminNo+1,XmaxNo)
        y = rd.randrange(YminNo+1,YmaxNo)
        inside = point_inside_polygon(x,y,poly)
    PointList[i] = [x,y]
    
    w.create_oval(x,y, x+10, y+10, outline="#f11", width=2,activefill="green")
    if i==1:
        w.create_line(x, y, PointList[0][0], PointList[0][1],fill="red", dash=(4, 4))
    if i>1:
        j = rd.randrange(i)
        w.create_line(x, y, PointList[j][0], PointList[j][1],fill="black", dash=(4, 4))
mainloop()

