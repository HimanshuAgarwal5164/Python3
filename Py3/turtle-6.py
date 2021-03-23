import turtle
wn=turtle.Screen()
alex=turtle.Turtle()
alex.color('blue')
alex.shape('turtle')
wn.bgcolor('green')
alex.up()
d=10
for i in range (0,20):
    alex.stamp()
    alex.forward(d)
    d=d+5
    alex.left(25)
wn.exitonclick()
