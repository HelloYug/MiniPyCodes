# Aesthetic Triangle and Square Rangoli (No Color)
# Author: Yug Agarwal

import turtle

# Initialize turtle
t = turtle.Turtle()
t.speed("fastest")

# Function to draw an equilateral triangle
def triangle():
    for _ in range(3):
        t.forward(200)
        t.left(120)

# Function to draw a square
def square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Drawing 240 rotated triangles
for _ in range(240):
    triangle()
    t.left(1.5)

# Drawing 120 rotated squares
for _ in range(120):
    square()
    t.left(3)

# To keep the window open (optional for some environments)
turtle.done()
