from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from random import randint
x=5
y=x
def isvalid(i,j):
    return i>=0 and i<x and j >=0 and j<y

def neighbours(i,j):
    out=[]
    for a in list(range(i-1,i+2)):
        for b in list(range(j-1,j+2)):
            if isvalid(a,b):
                out.append((a,b))
    out.remove((i,j))
    return set(out)

def CreateNeighbourHood():
    NeighbourHood={}
    for i in range(x):
        for j in range(y):
            NeighbourHood[(i,j)]=neighbours(i,j)
    return NeighbourHood

class Box(Button):
    NeighbourHood={}
    def __init__(self,i=-1,j=-1,n=0,Parent=None):
            Button.__init__(self,master=Parent,text=" ",width=4,height=2,command=self.pressed)
            self.i=i
            self.j=j
            self.n=n
            self.pack(side=LEFT,expand=YES,fill=BOTH)

    def getidx(self):
        return(self.i,self.j)
    def hasbomb(self):
        return self.n==9
    def placebomb(self):
        self.n=9
    def incrementNeighbours(self):
        if self.hasbomb():
            print(self.getidx())
            for u,v in Box.NeighbourHood[self.getidx()]:
                if not boxes[u][v].hasbomb():
                    boxes[u][v].n+=1

    def pressed(self):
        print(self.i,self.j)
        if self.hasbomb():
            if askokcancel("Game Over","You stepped on a mine"):
                #resetBox()
                pass
            else:
                root.quit()
        else:
            self.config(text=self.n)

root=Tk()
root.title("Minesweepyr")
root.minsize(360,360)
boxes=[]
def resetBox():
    global window
    try:
        window.destroy()
    except:
        pass
    for row in boxes:
        for k in row:
            k.destroy()
    window=Frame(master=root)
    window.pack(fill=BOTH,expand=YES)
    Box.NeighbourHood=CreateNeighbourHood()
    for i in range(x):
        r=Frame(master=window)
        r.pack(side=TOP,expand=YES,fill=BOTH)
        boxrow=[]
        for j in range(y):
            C=Box(i,j,Parent=r)
            boxrow.append(C)
        boxes.append(boxrow.copy())
    
    for k in range(x*y//6):
        i=randint(0,x-1)
        j=randint(0,y-1)
        while boxes[i][j].hasbomb():
            i=randint(0,x-1)
            j=randint(0,y-1)
        boxes[i][j].placebomb()
        boxes[i][j].incrementNeighbours()
resetBox()
root.mainloop()
