#input
cc= input ("Do you want to turn to dark mode: ")
print ("*"*20)

#importing library & other info
import turtle
t=turtle.Turtle()

#Color contrast conditioning
if cc=="Yes" or cc=="yes" or cc=="y":
    turtle.bgcolor("black")
    t.pen (pencolor="white")

if cc=="No":
    print ("Ok")
    
#other info

t.speed (10**1000)
t.pen (pensize="1.25")

#creating a function(s)
def triangle():
    for i in range (3):
        t.fd (250)
        t.left (120)

def square():
    for i in range (4):
        t.fd (125)
        t.rt (90)
        
def square2():
    for i in range (4):
        t.fd (75)
        t.rt (90)

#main program
for j in range (120):
    triangle()
    t.lt (3)

for j in range (60):
    square()
    t.lt (6)

for j in range (40):
    square2()
    t.lt (9)

t.pen (pensize="8")
t.penup()
t.fd (290)
t.pendown()
t.lt(90)
t.circle (290)


