#importing library & other info
import turtle
t=turtle.Turtle()
t.speed (15)
turtle.bgcolor ("black")

def trilogo():
    t.pen(fillcolor="white",pensize="3.5")
    for i in range (3):
        t.begin_fill()
        t.lt (30)
        t.fd (40)
        t.lt (70)
        t.fd (200)
        t.lt (160)
        t.fd (200)
        t.lt (70)
        t.fd (40)
        t.rt (90)
        t.end_fill()
        
def ring():
    t.pen(pensize="10",pencolor="white")
    t.penup()
    t.goto (0,-200)
    t.pendown()
    t.circle (200)

#creating Design
trilogo()
ring()

t.pen(pensize="2",pencolor="black")
'''
t.penup()
t.goto(0,200)
t.rt (90)
t.pendown ()
t.fd (160)
t.rt (60)
t.fd (40)
t.bk (40)
t.lt (120)
t.fd (40)

t.rt (60)
t.fd (40)
t.lt (60)
t.fd (160)
t.fd (-160)
t.rt (120)
t.fd (40)

t.rt (60)
t.fd (40)
t.lt (60)
t.fd (160)
t.fd (-160)
t.rt (120)
t.fd (40)
'''
t.lt (90)
t.penup()
t.goto (0,0)
t.pendown ()

t.fd (200)
t.fd (-200)
t.rt (120)

t.fd (200)
t.fd (-200)
t.rt (120)

t.fd (200)
t.fd (-200)
t.rt (120)
