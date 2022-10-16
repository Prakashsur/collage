import turtle
t=turtle.Turtle()
list=["yellow","red","green","blue"]
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(list[i])
    t.circle(50)
    t.end_fill()
    t.up()
    t.bk(100)
