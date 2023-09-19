import turtle 
from turtle import *
t = Turtle()


t.speed(0)
x = 10
def square():
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(90)
def row(z):
    for i in range(z):
        square()
        t.forward(x)



def pyramid():
    lines = 100 
    line = lines*x
    for i in range(lines):
        row(lines)
        t.right(90) 
        t.forward(x)
        t.left(90)
        t.back(line - x)
        t.left(90)
        t.forward(x*2)
        t.right(90)
        lines -= 1 
        line -= x 
pyramid()
    


turtle.done()