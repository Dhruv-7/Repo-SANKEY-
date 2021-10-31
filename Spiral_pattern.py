from turtle import *

bgcolor('black')
speed(0.2)
hideturtle()
for i in range(2000):
    color('red')
    circle(i)
    color('blue')
    circle(i*1.5)
    right(2)
    forward(1)
done()
