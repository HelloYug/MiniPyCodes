a=50
print ("-"*a)
print (("- Yug's Python Text Encrypter -").center(a))
print ("-"*a)
print ((" THE FILE IS PASSWORD PROTECTED ").center(a,"-"))
b= input("Enter your username: ")
c= input ("Enter your password: ")
count=0
while (b!= "yugla") or (c!= "1608"):
        print (("Either username or password mismatched").center (a,"-"))
        count+=1
        b= input("Enter your username: ")
        c= input ("Enter your password: ")
        if (b== "yugla") and (c== "1608"):
                continue
        if count==1:
                print ((" Intruders not Allowed ").center(a,"-"))
                print ((" WARNING! "*3).center(a,"-"))
                print ((" Just Get Out! ").center(a,"-"))
                break
else:
        print ("\tlogging in...")
        print ("*"*a)
        d= str (input ("Enter Text: "))
        d= d.strip()
        print ("Text to be Encryped: ", d)
        if (len(d)%2) == 1:
                d += "_"
        e= d[::-1]
        from random import choice
        from string import yugmix
        f= list (yugmix)
        g= f.remove ("_" and "^" and "$")
        h= ""

        for i in range(0, len(e), 2):                 
                j= str (choice(f))
                k= e[i:i + 2]+ j
                h+= k
        l=1
        m=len (h)
        if m%2 == 1:
                m += 1
        n= []
        for j in range (int (m/2)):
                try:
                        n.append (h[l])
                        l-=1
                        n.append (h[l])
                        l+=3
                except IndexError:
                        pass
        if m%2 == 1:
                n.append (h[-1])
        o= len (n)
        from random import randint
        for k in range (o//5):
                p= randint (0,o-1)
                q= randint (0,o-1)
                n.insert (p, "^")
                n.insert (q, "$")
        r= "".join(n)
        print ("Encrypted Text:", r)
        print ("-"*a)

'''
a=width
b=username
c=pwd
d=string
e=invertedsentence
f=listofyugmix
g=updatedlistofyugmix
h=randomizedsentence
i=<skip>
j=char
k=randomizedadding
l= initialindex
m= lrs(length of randomizedsentence)
n= Encryptedlist
o= lambai
p= index
q= index2
r= Encrypted_text
'''
