import turtle
from turtle import *
t = Turtle()
t.speed(1000000)
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)


""" for i in range(4):
    square(40) """
def triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)
""" triangle(50) """
def star(x):
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)

""" starlength = 50
for i in range(60):
    star(starlength)
    t.right(5)
    starlength = starlength+5
 """
length = 50
for i in range(60):
    square(length)
    t.right(5)
    length = length + 10

turtle.done()