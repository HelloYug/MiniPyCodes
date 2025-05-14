# Mercedes Logo Design using Turtle Graphics
# Author: Yug Agarwal

import turtle

# Setup
t = turtle.Turtle()
t.speed(15)
turtle.bgcolor("black")

# Function to draw the white triangular logo
def trilogo():
    t.pen(fillcolor="white", pensize=3.5)
    for _ in range(3):
        t.begin_fill()
        t.left(30)
        t.forward(40)
        t.left(70)
        t.forward(200)
        t.left(160)
        t.forward(200)
        t.left(70)
        t.forward(40)
        t.right(90)
        t.end_fill()

# Function to draw the outer ring
def ring():
    t.pen(pensize=10, pencolor="white")
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(200)

# Drawing the logo
trilogo()
ring()

# Drawing the three inner spokes of the Mercedes logo
t.pen(pensize=2, pencolor="black")
t.left(90)
t.penup()
t.goto(0, 0)
t.pendown()

for _ in range(3):
    t.forward(200)
    t.backward(200)
    t.right(120)

# Optional: keep window open
turtle.done()
