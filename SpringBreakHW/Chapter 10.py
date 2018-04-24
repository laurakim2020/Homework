#Problem 1
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
n=1

def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()

def r():
    tess.color("red")

def g():
    tess.color("green")

def b():
    tess.color("blue")

def h5():
    global n
    tess.pensize(n)
    n += 1
    if n > 20:
        n = 20
    return n

def h6():
    global n
    n -= 1
    if n < 1:
        n = 1
    tess.pensize(n)
    return n

def h7():
    turtle.dot(100,"red")

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(r, "r")
wn.onkey(g, "g")
wn.onkey(b, "b")
wn.onkey(h5, "+")
wn.onkey(h6, "-")
wn.onkey(h7, "d")

wn.listen()
wn.mainloop()

