import turtle
wn=turtle.Screen()
wn.bgcolor('green')
alex=turtle.Turtle()
alex.color('red')
alex.pensize(5)
john=turtle.Turtle()
john.color('blue')
for x in range (0,4):
    alex.forward(100)
    alex.left(90)
john.right(90)
for x in range (0,3):
    john.left(60)
    john.forward(100)
    john.left(60)
