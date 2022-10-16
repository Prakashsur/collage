def cir(x,y,clr,rad):
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(clr)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()

import turtle
t=turtle.Turtle()
t.up()
cir(0,-50,"green",50)
cir(200,100,"orange",50)
cir(-200,100,"blue",50)
cir(-200,-100,"red",-50)
cir(200,-100,"yellow",-50)
t.sleep(30)