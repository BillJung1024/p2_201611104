import turtle
import math
import random


wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.bgpic("space.gif")
wn.tracer(3)

mypen= tubrtle.Turtle()
mypen.penup()
mypen.setpos(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.fd(600)
    mypen.left(90)
mypen.hideturtle()

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