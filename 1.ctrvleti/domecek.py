import turtle
import random
t = turtle

colors = ["purple", "green", "red", "yellow", "brown"]



def color():
    return random.choice(colors)

def zeme():
    t.left(180)
    t.forward(300)
    t.penup()
    t.right(180)
    t.forward(100)

def domecek(vyska, sirka, barva):

    t.pencolor(barva)
    t.pendown()
    t.left(90)
    t.forward(vyska)
    t.right(45)
    t.forward(vyska)
    t.right(90)
    t.forward(vyska)
    t.right(135)
    t.forward(sirka)
    t.right(180)
    t.penup()
    t.forward(sirka)
    t.right(90)
    t.pendown()
    t.forward(vyska)
    t.penup
    t.left(90)
    t.forward(5)
    t.pendown()





zeme()
domecek(70,100, "blue")
domecek(25,35, "green")
domecek(35,50, "red")

t.exitonclick()