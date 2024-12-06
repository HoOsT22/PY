import turtle


s = turtle

size = 150


def pentagram(size):
    for x in range(5):
        s.forward(size)
        s.right(144)



pentagram(80)

s.left(90)

for x in range(360):
    s.right(72)
    s.forward(80)



s.exitonclick()