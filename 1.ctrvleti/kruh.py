import random 
import turtle 
z = turtle
colors = ["red", "green", "silver", "pink", ]

def color():
    return random.choice(colors)

def kruh():
    z.fillcolor(color())
    z.begin_fill()
    z.circle(80)
    z.end_fill()

#kruh()
    
def trj():
    z.fillcolor(color())
    z.begin_fill()
    for x in range(3):
        z.forward(100)
        z.left(120)
    z.end_fill()

#trj()
    


z.exitonclick()