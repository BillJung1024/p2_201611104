import turtle
import math
import random


wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.tracer(3)
mypen= turtle.Turtle()




def fileset():
    File='makeSquare.txt'
    file=open('makeSquare.txt','r')
    file.close()
fileset()

Afile=raw_input("input yout file: makeSquare.txt")
frec=open(Afile)
coords=list()
for line in frec:
    line1=line.split(',')
    coords.append([(line1[0],line1[1]),(line1[2],line1[3]),(line1[4],line1[5]),(line1[6],line1[7].strip())])
    print coords
frec.close()
def makeSquare(coords):
    for coord in coords:
        x1=int(coord[0][0])
        y1=int(coord[0][1])
        x2=int(coord[1][0])
        y2=int(coord[1][1])
        x3=int(coord[2][0])
        y3=int(coord[2][1])
        x4=int(coord[3][0])
        y4=int(coord[3][1])
        mypen.penup()
	mypen.goto(x1,y1)
	mypen.pendown()
        mypen.pensize(3)
	mypen.goto(x2,y2)
	mypen.goto(x3,y3)
	mypen.goto(x4,y4)
        mypen.hideturtle()
        
makeSquare(coords)
        
     
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)

maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("green")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setpos(random.randint(-300,300),random.randint(-300, 300))





def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)
    
def increasespeed():
    global speed
    speed += 1
    
def isCollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1,ycor()-t2.ycor(),2))
    if d< 20:
        return True
    else:
        return False
    
    
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")

speed = 1

while True:
    player.fd(speed)
    
    if player.xcor()> 290 or player.xcor()< -290:
        player.right(180)
        
    if player.ycor()>290 or player.ycor()<-290:
        player.right(180)
    
   
        
    for count in range(maxGoals):
        goals[count].fd(3)

        if goals[count].xcor()> 290 or goals[count].xcor()< -290:
            player.right(180)

        if goals[count].ycor()>290 or goals[count].ycor()<-290:
            player.right(180)
            
        if isCollision(player,goals[count]):    
            goals[count].setpos(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))