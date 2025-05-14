# Multi-Shape Rangoli Design with Optional Dark Mode
# Author: Yug Agarwal

import turtle

# Ask user for theme preference
cc = input("Do you want to turn to dark mode? (yes/no): ")
print("*" * 20)

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.pen(pensize=1.25)

# Dark mode configuration
if cc.lower() in ["yes", "y"]:
    turtle.bgcolor("black")
    t.pen(pencolor="white")
else:
    print("Ok")

# Function to draw an equilateral triangle
def triangle():
    for _ in range(3):
        t.forward(250)
        t.left(120)

# Function to draw a square
def square():
    for _ in range(4):
        t.forward(125)
        t.right(90)

# Function to draw a smaller square
def square2():
    for _ in range(4):
        t.forward(75)
        t.right(90)

# Drawing multiple rotated triangles
for _ in range(120):
    triangle()
    t.left(3)

# Drawing multiple rotated squares
for _ in range(60):
    square()
    t.left(6)

# Drawing multiple smaller rotated squares
for _ in range(40):
    square2()
    t.left(9)

# Drawing the outer border circle
t.pen(pensize=8)
t.penup()
t.forward(290)
t.pendown()
t.left(90)
t.circle(290)

# Optional: keep the window open
turtle.done()
