a=50
print ("-"*a)
print (("- Yug's Python Text Decrypter -").center(a))
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
        d= input ("Enter Text: ")
        print ("Text to be Decrypted:", d)
        e= ""
        for i in d:
            if i!="^":
                e += i
        f= ""        
        for j in e:
            if j!="$":
                f += j
        if len(f)%2 == 1:
            h= str (f[-1])
            g = f[:len (f)-1]
        else:
            g = f
        i= 1
        j= []
        for k in range (int (len(g)/2)):
                        j.append (g[i])
                        i-=1
                        j.append (g[i])
                        i+=3
        if len(f)%2 == 1:
            j.append (h)
        for i in range (2, len(j), 2):
            try:
                del j[i]
            except IndexError:
                pass
        k= "".join(j)
        if k[0] == "_":
            l= k [1:]
        else:
            l= k
        m = l[::-1]
        print ("\nDecrypted text: ", m)
        print ("-"*a)
        
'''
a= width
b= username
c= pwd
d= string
e= string1
f= string2
g= string3
h= alpha
i= initialindex
j= encrypttorandomised
k= unrandomizedtext
l= uninvertedtext
m= Decrypted_text
'''
