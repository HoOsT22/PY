import random 
import turtle

kik = turtle
colors = ["purple", "green", "red", "yellow", "brown"]


def color():
    return random.choice(colors)


def square():
    kik.fillcolor(color())
    kik.begin_fill()
    for x in range (4):
        kik.forward(90)
        kik.left(90)
    kik.end_fill()

square()
color()



kik.exitonclick()
