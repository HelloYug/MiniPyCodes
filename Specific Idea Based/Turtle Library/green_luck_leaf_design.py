# Luck Leaf Design using Turtle Graphics
# Author: Yug Agarwal

from turtle import *

# Setup
color("green")
speed(100)
pensize(20)

# Draw 4 symmetrical leaf shapes to form a lucky leaf
for _ in range(4):
    begin_fill()
    left(50)
    forward(135)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(135)
    end_fill()
    right(40)

# Optional: keeps the window open
done()
