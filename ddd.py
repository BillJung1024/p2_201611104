import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def varamgebi(size,bigger,turns,sides,angle):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
varamgebi(30,20,10,50,90)
wn.exitonclick()