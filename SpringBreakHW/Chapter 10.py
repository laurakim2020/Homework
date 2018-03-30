#Problem 1
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
sn=1

def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()

def h5():
    tess.color("Red")

def h6():
    tess.color("Green")

def h7():
    tess.color("Blue")

def h8():
    global sn
    tess.pensize(sn)
    sn += 1
    if sn > 20:
        sn = 20
    return sn

def h9():
    global sn
    sn -= 1
    if sn < 1:
        sn = 1
    tess.pensize(sn)
    return sn

def h10():
    turtle.dot(100,"red")

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "R")
wn.onkey(h6, "G")
wn.onkey(h7, "B")
wn.onkey(h8, "+")
wn.onkey(h9, "-")
wn.onkey(h10, "d")

wn.listen()
wn.mainloop()
