#Python program to draw spiral square in turtle programming
import turtle 
t = turtle.Turtle()

side = 200
for i in range(50):
   t.forward(side)
   t.right(90) #Exterior angle of a square is 90 degree
   side = side - 4
