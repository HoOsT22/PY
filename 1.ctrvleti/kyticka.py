import turtle
import random


tt = turtle
colors = ["purple", "green", "red", "yellow", "brown"]

def color():
    return random.choice(colors)

def stonek():
    tt.left(90)
    tt.forward(150)
    tt.right(180)
    tt.forward(75)


def listy():

    tt.fillcolor(color())
    tt.begin_fill()
    tt.right(90)
    tt.forward(50)
    tt.left(140)
    tt.forward(65)
    tt.left(80)
    tt.forward(65)
    tt.left(140)
    tt.forward(50)
    tt.end_fill()


def kruh():

    tt.fillcolor(color())
    tt.begin_fill()
    tt.right(90)
    tt.forward(75)
    tt.right(90)
    tt.circle(50)
    tt.end_fill()
    tt.penup()
    tt.left(90)
    tt.forward(20)
    tt.pendown()
    tt.fillcolor(color())
    tt.begin_fill()
    tt.right(90)
    tt.circle(30)
    tt.end_fill()
    tt.penup()
    tt.left(90)
    tt.forward(20)
    tt.pendown()
    tt.fillcolor(color())
    tt.begin_fill()
    tt.right(90)
    tt.circle(10)
    tt.end_fill()

stonek()
listy()
color()
kruh()

tt.exitonclick()


