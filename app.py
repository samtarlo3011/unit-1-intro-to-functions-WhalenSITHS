import turtle
from turtle import *
t = Turtle()

t.speed('fastest')
def square(sidelength):
    '''Draws a square of a
    given sidelength'''
    for i in range(4):
        forward(sidelength)
        right(90)

""" def square(sidelength):
    '''Draws a square of a
    given sidelength'''
    for i in range(4):
        forward(sidelength)
        right(90)
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length)
        length = length +5 
        t.right(5)
addSquares(60) """
def star(x, y):
    for i in range(5):
        t.forward(x)
        t.left(y)

def star_spiral(x):
    length = 5
    for i in range(x):
        star(length,144)
        t.right(5)
        length += 5
star_spiral(60)



turtle.done()
