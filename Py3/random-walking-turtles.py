import turtle
import random

def check(x,y,w,h):
    if x >= -w/2 and x <= w/2:
        if y <= h/2 and y >= -h/2:
            return True
    return False



wn=turtle.Screen()
wn.bgcolor('green')
width=wn.window_width()
height=wn.window_height()

alex=turtle.Turtle()
alex.color('red')
alex.shape('turtle')
x=alex.xcor()
y=alex.ycor()
while check(x,y,width,height):
    r=random.randint(0,1)
    if r==0:
        alex.left(90)
        alex.forward(50)
    else:
        alex.right(90)
        alex.forward(50)
    x=alex.xcor()
    y=alex.ycor()
    
wn.exitonclick()
