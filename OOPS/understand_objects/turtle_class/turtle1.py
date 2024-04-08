import turtle

# creating two objects 
t1 = turtle.Turtle()
t2= turtle.Turtle()

#assigning a color property/method to each object
t1.color("orange")
t2.color("green")

#method to object1
t1.forward(50)
t1.left(90)

#method to object2
t2.left(90)
t2.forward(50)

#allows the drawing to stay on screen once done
turtle.done()