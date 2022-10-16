import turtle
t=turtle.Turtle()
list=["purple","yellow","orange","red","green","black"]
for i in range(200):
    t.color(list[i%6])
    t.pensize(i/11+1)
    t.forward(i)
    t.left(59)