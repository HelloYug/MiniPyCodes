from libtype import heading
heading (["Love Percentage Caluclator"], "*", "*", 60)

na = input ("Enter Partner 1 Name: ").strip()
nb = input ("Enter Partner 2 Name: ").strip()

def getL(n):
    n = list(n)
    l = []
    count = 0
    for i in n[0::]:
        for j in n[0::]:
            if j == i:
                count += 1
                n.remove(i)
        if count != 0:
            l.append(count)
        count = 0

    return l

def loop(l):
    a = 1
    if len(l) % 2  == 0:
        a = 0

    k = []
    for i in range (len(l)//2 + a):
        if len (l) > 1:
            k.append (str(int(l[0]) + int(l[-1])))
            l.pop(0)
            l.pop(-1)

        else:
            k.append(str(int(l[0])))
            break

    k = list("".join(k))
    return k

def CLP(l):
    j = loop (getL(l))
    while len (j) != 2:
        j = loop(j)
    return int("".join(str(o) for o in j))

d = CLP((na + "LOVES" + nb).upper())
print ("\n" + (na + " LOVES " + nb).upper())
print (f"Your Love percentage is {d}%.\n")

H = CLP((nb + "LOVES" + na).upper())
print ((nb + " LOVES " + na).upper())
print (f"Your Love percentage is {H}%.\n")

print (f"Your Mutual Love percentage is {(d+H)/2}%.")

print ("*"*60)