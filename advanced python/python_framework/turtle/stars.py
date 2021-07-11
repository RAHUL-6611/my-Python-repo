import turtle
import math
import random


fool = turtle.Turtle()
turtle.shape("turtle")
fool.getscreen().bgcolor('#0066AF')

fool.penup()
fool.goto(-100,200)
fool.pendown()

fool.speed(2000)
fool.color("red", "yellow")

def star(panda, size, color):
    if size<= 10:
     return
     
    else:
     fool.begin_fill()
    for i in range(5):
     panda.forward(size)
     star(turtle, size/3,"#FFFF00")
     panda.left(216)
     panda.color(color)

    fool.begin_fill()


star(fool, 360, "#FFFF00")

turtle.done()