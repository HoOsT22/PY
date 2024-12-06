import turtle
import random

tt = turtle
colors = ["purple", "green", "red", "yellow", "brown"]

def color():
    return random.choice(colors)



def random_position():
    tt.penup()
    tt.goto(random.randint(-200, 200), random.randint(-200, 200))
    tt.pendown()
    
def n_uhelnik():
    strany = random.randint(3, 10)  
    uhel = 360 / strany  
    delka = random.randint(50, 150)  
    
    random_position()   



    for x in range(strany):
        tt.forward(delka)
        tt.left(uhel)

color()
n_uhelnik()

turtle.done()

tt.exitonclick
