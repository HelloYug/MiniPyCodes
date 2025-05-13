#inputs
a= int (input ("Enter side length: "))
cc= input ("Do you want to turn to dark mode: ")

'''
print ("\nEnter the letters of your name in different lines")
char= input ("Char: ")
while char!=str:
    char= input ("Char: ")
    if char=="":
        break
'''
#importing libraries and other info
import turtle
t=turtle.Turtle()
t.speed (5)

#creating functions
def goto(x,y):
    t.penup()
    t.goto (x,y)
    t.pendown()
    
def y():
    goto (-(14*a/8),0)
    t.lt (90)
    t.fd (a/2)
    
    t.rt (90)
    t.fd (a/3)

    t.rt (90)
    t.fd (a/8)
    t.circle (a/6,180)
    t.fd (a/8)

    t.rt (90)
    t.fd (a/3)

    t.rt (90)
    t.fd (a/2)

    t.rt (90)
    t.fd (a/3)

    t.lt (90)
    t.fd (a/2)

    t.rt (90)
    t.fd (a/3)

    t.rt (90)
    t.fd (a/2)

    t.lt (90)
    t.fd (a/3)

    t.rt (90)

def u():
    goto(-(a/2),-(a/2))
    t.fd (a)

    t.rt (90)
    t.fd (a/3)

    t.rt (90)
    t.fd (2*a/3)

    t.lt (90)
    t.fd (a/3)

    t.lt (90)
    t.fd (2*a/3)

    t.rt (90)
    t.fd (a/3)

    t.rt (90)
    t.fd (a)

    t.rt (90)
    t.fd (a)

    t.rt (90)

def g():
    goto (3*a/4,-(a/2))
    t.fd (a)

    t.rt (90)
    t.fd (4*a/5)

    t.rt (90)
    t.fd (2*a/5)

    t.rt (90)
    t.fd (a/5)

    t.rt (90)
    t.fd (a/5)

    t.lt (90)
    t.fd (2*a/5)

    t.lt (90)
    t.fd (3*a/5)

    t.lt (90)
    t.fd (a/5)

    t.lt (90)
    t.fd (a/5)

    t.rt (90)
    t.fd (3*a/5)

    t.rt (90)
    t.fd (2*a/5)
    
    t.rt (90)
    t.fd (a/5)

    t.rt (90)
    t.fd (a/5)

    t.lt (90)
    t.fd (a/5)

    t.lt (90)
    t.fd (a/5)

    t.rt (90)
    t.fd (3*a/5)

    
#calling functions
if cc=="Yes" or cc=="yes" or cc=="y":
    turtle.bgcolor("black")
    t.pen (fillcolor="white")
    print ("Ok")

if cc=="No" or cc=="n":
    print ("Ok")
    t.pen (fillcolor="black")

#if char=="y":
t.begin_fill()
y()
t.end_fill()
    
#if char=="u":
t.begin_fill()
u()
t.end_fill()

#if char=="g":
t.begin_fill()
g()
t.end_fill()
