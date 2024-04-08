#this program lets a user draw a star or circle
import turtle

def star(t1,col,size,wid):
    t1.color(col)
    t1.width(wid)

    t1.begin_fill()
    for i in range(5):
        t1.forward(size)
        t1.left(144)
    t1.end_fill()

def circle(t1,rad,color):
    t1.color(color)
    t1.begin_fill()
    t1.circle(rad)
    t1.end_fill()

t = turtle.Turtle()
shape = input("Enter the shape (star,circle). Enter no to stop: ")
while shape !="no":
    try:
        if shape == "star":
            col = input("Enter the colour: ")
            size = int(input("Enter the size of star: "))
            width = int(input("Enter the width: "))
            star(t,col,size,width)
        elif shape == "circle":
            col = input("Enter the colour: ")
            radius = int(input("Enter the radius of the circle : "))
            circle(t,radius,col)
        else: 
            print("please enter the valid shape!!")
        shape = input("Enter the shape (star,circle). Enter 'no' to stop: ")
    except:
        print("error occured")
        shape = input("Enter the shape (star,circle). Enter 'no' to stop: ")

