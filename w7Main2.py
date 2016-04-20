import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
x=list()

def drawSquareAt(size, pos): 
    t1.penup() 
    t1.setpos(size)
    t1.pendown() 
    for i in range(0,4):
        tracks=append(t1.pos())
        t1.forward(size) 
        t1.right(90) 
    return tracks

def lab7a():
    mytrack=drawSquareAt(size,pos)
    print mytrack

import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
c=dict() 
c=({0:(0,0),1:(100,0),2:(100,100),3:(0,100),4:(0,0)}) 

def lab7b(): 
	for i in range(1,5): 
		t1.goto(c[i]) 
	for j in range(1,5): 
 		print c[j] 
    
    
def main():
    lab7a()
    lab7b()
    