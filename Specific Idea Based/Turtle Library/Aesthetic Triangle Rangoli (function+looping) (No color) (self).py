#importing of module &other info
import turtle
t=turtle.Turtle()

#creating a function(s)
def triangle():
    for i in range (3):
        t.fd (200)
        t.left (120)

def square():
    for i in range (4):
        t.fd (100)
        t.rt (90)

#main program
t.speed ("fastest")
for j in range (240):
    triangle()
    t.lt (1.5)

for j in range (120):
    square()
    t.lt (3)
