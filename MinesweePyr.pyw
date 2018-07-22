from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from random import choice
        
x=7
y=x
def isvalid(i,j):
    return i in list(range(x)) and j in list(range(y))
def neighbours(i,j):
    out=[]
    for a in list(range(i-1,i+2)):
        for b in list(range(j-1,j+2)):
            if isvalid(a,b):
                out.append((a,b))
    out.remove((i,j))
    return out

row=[]
game=[]
def resetgrid(a,b):
    global x,y,row,game
    x=a
    y=b
    for i in range(x):
            row.append(0)
    for j in range(y):
            game.append(row.copy())
    for i in game: print(i)
    for k in range(10):
        i=choice(list(range(a)))
        j=choice(list(range(b)))
        while game[j][i]==9:
            i=choice(list(range(a)))
            j=choice(list(range(b)))
        print(i,j)
        game[j][i]=9

resetgrid(6,8)
for i in game: print(i)


def endprg():
    if askyesno("Quit?","Do you really want to quit?"):
       root.quit
       root.destroy()
    else:
       pass
def resetmsg():
   if askokcancel("Reset?","Start new game?"):
      reset()

class row:
    def __init__(self,p):
        self=Frame(p)
        self.pack(side=TOP)
class col:
    def __init__(self,p):
        self=Frame(p)
        self.pack(side=TOP)


class box:
    def __init__(self,i,j,n=0,Parent=None,adj=[]):
        self.i=i
        self.j=j
        self.n=0
        self.adjacent=neighbours()
        for x in adj:
            self.adjacent.append(x)
    def hasbomb(self): return n==9
    def placeBomb(self):
        self.n=9

boxes=[]
for i in list(range(x)):
    for j in list(range(y)):
        boxes.append(box(game[j][i]))

root=Tk()
root.title("Minesweepyr")
main=Frame(root)
main.pack(expand=YES)
File=Menu(main)
