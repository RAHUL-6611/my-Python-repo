import turtle
import math
import random


fool = turtle.Turtle()
turtle.shape("turtle")
fool.getscreen().bgcolor('#000000')

fool.speed(200)
fool.color("red", "yellow")

# fool.pencolor("#000066")
fool.pensize(2)
fool.begin_fill()


# def boxx(fool):

for me in range(98):

    fool.forward(200)
    fool.forward(math.sin(me/20)*50)
    # fool.forward(math.sqrt(me)*4)
    # fool.left(me%200)
    fool.left(90)

fool.end_fill()

fool.penup()
fool.forward(200)

fool.pendown()

# boxx(fool)
fool.left(220)

turtle.done()
