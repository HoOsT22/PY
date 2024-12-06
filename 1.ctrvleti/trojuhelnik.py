import random
import turtle
j = turtle

pocet = [3,4,5,6,7]
delka = 50
delka2 = 25

for x in range (25):
    j.left(360/random.choice(pocet))
    j.forward(delka)
    delka += 5

j.penup()
j.right(90)
j.forward(300)
j.pendown()

for x in range (25):
    j.left(360 /random.choice(pocet))
    j.forward(delka2)
    delka2 += 5


j.exitonclick()