while True:
    num= input("Enter a Binary Number: ")

    while True:
        t = set(num)
        b = {'0','1'}
        if b == t or t == {'0'} or t == {'1'}:
            break
        
        else:
            num= input("Enter a Binary Number: ")

    Sum=0
    power=len(num)-1
    nole=1 #no of loop execution
    for i in num[::1]:
        y= int (i)*(2**power)
        power-=1
        if len(num)-1>=nole:
            print (y, end="+")
        else:
            print (y, end="")

        nole+=1
        Sum= Sum + y
        
    print ("\n\nBinary to Decimal Conversion: ",Sum)
