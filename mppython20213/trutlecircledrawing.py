from turtle import *
t=Turtle()
w=Screen()
w.setup(800,600)
'''
t.circle(50) # anticlock wise
t.circle(-50)  # clockwise
t.undo()
t.circle(100)
t.reset()
'''
t.circle(100,steps=10)
t.circle(-75,extent=180)
t.up()
t.goto(50,100)
t.down()
t.circle(200)
t.write("This is Done by me",font=("Comic Sans MS",15))
done()