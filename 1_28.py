import turtle
from turtle import *
t = Turtle()
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)


""" for i in range(4):
    square(40) """
def triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)
""" triangle(50) """


turtle.done()