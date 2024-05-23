from turtle import *
t=Turtle()
color_list=['red','yellow','green','blue','orange']
d=300
for i in range(200):
    t.color(color_list[i%5])
    t.forward(d)
    t.left(144)
    d=d-3
done()