# Draw the name "YUG" using Turtle graphics
# Author: Yug Agarwal

import turtle

# Input from user
a = int(input("Enter side length: "))
cc = input("Do you want to turn to dark mode? (yes/no): ")

# Turtle setup
t = turtle.Turtle()
t.speed(5)

# Apply dark mode if selected
if cc.lower() in ["yes", "y"]:
    turtle.bgcolor("black")
    t.fillcolor("white")
    print("Dark mode activated.")
else:
    t.fillcolor("black")
    print("Light mode activated.")

# Helper function to move turtle
def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw 'Y'
def draw_y():
    goto(-(14 * a / 8), 0)
    t.left(90)
    t.forward(a / 2)

    t.right(90)
    t.forward(a / 3)
    t.right(90)
    t.forward(a / 8)
    t.circle(a / 6, 180)
    t.forward(a / 8)

    t.right(90)
    t.forward(a / 3)
    t.right(90)
    t.forward(a / 2)
    t.right(90)
    t.forward(a / 3)

    t.left(90)
    t.forward(a / 2)
    t.right(90)
    t.forward(a / 3)
    t.right(90)
    t.forward(a / 2)
    t.left(90)
    t.forward(a / 3)
    t.right(90)

# Draw 'U'
def draw_u():
    goto(-(a / 2), -(a / 2))
    t.forward(a)
    t.right(90)
    t.forward(a / 3)
    t.right(90)
    t.forward(2 * a / 3)
    t.left(90)
    t.forward(a / 3)
    t.left(90)
    t.forward(2 * a / 3)
    t.right(90)
    t.forward(a / 3)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)

# Draw 'G'
def draw_g():
    goto(3 * a / 4, -(a / 2))
    t.forward(a)
    t.right(90)
    t.forward(4 * a / 5)
    t.right(90)
    t.forward(2 * a / 5)
    t.right(90)
    t.forward(a / 5)
    t.right(90)
    t.forward(a / 5)

    t.left(90)
    t.forward(2 * a / 5)
    t.left(90)
    t.forward(3 * a / 5)
    t.left(90)
    t.forward(a / 5)
    t.left(90)
    t.forward(a / 5)

    t.right(90)
    t.forward(3 * a / 5)
    t.right(90)
    t.forward(2 * a / 5)
    t.right(90)
    t.forward(a / 5)
    t.right(90)
    t.forward(a / 5)

    t.left(90)
    t.forward(a / 5)
    t.left(90)
    t.forward(a / 5)
    t.right(90)
    t.forward(3 * a / 5)

# Drawing each letter with fill
t.begin_fill()
draw_y()
t.end_fill()

t.begin_fill()
draw_u()
t.end_fill()

t.begin_fill()
draw_g()
t.end_fill()

# Keep window open
turtle.done()
