from turtle import *
t=Turtle()   # we are creating Turtle class object
def drawmyshape():
    for i in range(4):
        t.fd(200)
        t.left(90)
w=Screen()
w.title("My First Turtle Program")
#w.bgcolor("red")
#w.bgpic('turtle.gif')
t.color('red','yellow')
t.shape('turtle')
t.pensize(5)
#t.hideturtle()
t.speed(1)
'''for i in range(4):
    t.fd(100)
    t.left(90)
'''
drawmyshape()
t.right(90)

'''
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
#t.penup()
t.pu()
t.fd(100)
t.pendown()
t.color('blue','orange')
t.begin_fill()
drawmyshape()
'''
for i in range(4):
    t.fd(100)
    t.left(90)
'''
'''t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
'''
t.end_fill()
done()