#check whether N is prime or not in given range
#other info
width=35
prime=[]

#heading
print ("~"*width)
#print (("EXPERIMENT NO. 06").center (width))
print (("Finding Prime Numbers").center (width))
print ("~"*width)
print ()

#inputs
N = int (input ("Enter the first number: "))
N2= int (input ("Enter the Second number: "))
print ("*"*width)

if N2<N:#did this coz (chai aur coffee ke glass ko interchange karna hai to ek khali mug lenge na)
    c=N
    N=N2
    N2=c
    # N, N2 = N2, N

#conditioning and printing output
for K in range (N,N2+1):
    if K<=1: #1 is neither prime nor composite
        continue
    
    light="Off"
    for i in range (2, int(K/2)+1):#if not a prime number
        if K%i==0:
            light="on"
            break
         
    if light=="Off":#if a prime number
        if K<N2:
            prime.append (K)

if len (prime)==1:
    pro = "is "
else:
    pro = "are "
    
#if no prime numbers found in the given range
if len (prime)==0:
    print ("There are no prime numbers between the given range!")
    
else:
    print ("Prime numbers between", N, "&", N2, pro,end="")
    print (*prime, sep=",",end="")
    print (".")
