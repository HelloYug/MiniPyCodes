# other info
width = 50

# heading
print ('*'*width)
print ('Find Pythagorean Triplet of'.center(width))
print ('*'*width)

print ("\nFormula --> (2m, m\u00b2-1, m\u00b2+1)\n")
# inputs
while True:
    n = int (input ("Enter number: "))
    if n > 1:
        break

print ("\nPlease select which is the number;")
print ("\t1. Smallest side (2m)")
print ("\t2. Middle side (m\u00b2-1)")
print ("\t3. Hypotenuse (m\u00b2+1)")

while True:
    choice = int (input ("Enter your choice: "))
    if 0 < choice < 4:
        break

if choice == 1:
    m = round(n/2, 3)

if choice == 2:
    m = round((n + 1)**0.5, 3)

if choice == 3:
    m = round((n - 1)**0.5, 3)

# main program
a = round (2*m, 3)
b = round ((m**2)-1, 3)
c = round ((m**2)+ 1, 3)
PT = [a, b, c]
PT.sort()

# printing output
print (f"\n-> {PT[0]}\u00b2 + {PT[1]}\u00b2 = {PT[2]}\u00b2")
print (f"-> {(PT[0])**2} + {(PT[1])**2} = {(PT[2])**2}")
print (f"::: Hence, Pythagorean Triplet --> ({PT[0]}, {PT[1]}, {PT[2]})")
print ('*'*width)  # Finishing line