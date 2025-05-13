#other info
width= 60

#heading
print ("~"*width)
print (("Python Turtle Pie Chart").center (width))
print ("~"*width)

#inputs
x= input("Enter the partitions seperated by comma(,): ")
y= int (input ("Enter the radius of pie chart: "))
print ("Creating your data pie chart...\n")

#other info
from random import choice
l= x.split(",")
vr = [
    '#9400D3',#V
    '#4B0082',#I
    '#0000FF',#B
    '#00FF00',#G
    '#FFFF00',#Y
    '#FF7F00',#O
    '#FF0000',#R
    ]
print (l)
#loop for sum
Sum= 0
for i in range(len(l)):
    Sum+=(abs (int(l[i])))

#finding angles
ang=[]
for j in range(len(l)):
    ang.append (((abs(int(l[j])))/Sum)*360)
    
#importing module
import turtle
t= turtle.Turtle()
t.speed (6)
t.pen (pensize= "3.5")

#making pie chart
t.ht()
for k in range (len(l)):
    t.pen(fillcolor= choice (vr)) #colorfill
    t.begin_fill()
    if k==0:
        t.fd (y)
        t.lt (90)
    t.circle (y,ang[k])
    t.goto (0,0)
    t.end_fill()
    print ("Partition", (k+1),": ", str(round(((abs(int(l[k])))/Sum)*100,3))+" %")
    t.lt (90)
    t.bk (y)
    t.rt (90)
