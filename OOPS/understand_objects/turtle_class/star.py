import turtle

t1= turtle.Turtle()

t1.color("orange")
t1.width(5)

t1.begin_fill()
for i in range(5):
    t1.forward(150)
    t1.left(144)
t1.end_fill()

turtle.done()