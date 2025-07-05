# Python program to demonstrate spiral circle drawing
#importing library
import turtle
t = turtle.Turtle()
t.speed (20)
t.pen (pensize="2")

# taking radius of initial radius
r = 5

# Loop for printing spiral circle
for i in range(100):
	t.circle(r + i, 45)
