#importing modules
import random
from libtype import AniType

#other info
width=35

#heading
print ("-"*width)
print (("Kundli Match Maker").center(width))
print ("-"*width)

#inputs
n1= input ("Enter Your Name \t : ")
n2= input ("Enter Your Partner's name: ")
print ()

#processing
res= random.randint (8,36)

#printing output
print (f"Aapke {res} Gun milte hain!")
hehe= "-"*(int((res-5)/4))

print ("[",end="")
AniType(hehe,0.03,0.2)
print (f" {res} ",end="")
# print (res,"% ",end="")
AniType(hehe,0.03,0.2)           
print ("]")

print (n1,"❤", n2)
