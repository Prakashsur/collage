import turtle
import time
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.color("white")
t.hideturtle()
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90,200)
t.left(120)
t.circle(-90,200)
t.forward(180)
t.end_fill()
time.sleep(10)
