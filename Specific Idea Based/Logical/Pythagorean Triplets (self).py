# other info
width = 50

# heading
print ('*'*width)
print ('Pythagorean Triplets'.center(width))
print ('*'*width)

print ("Formula --> (2m, m\u00b2-1, m\u00b2+1)\n")

# inputs
while True:
    n = int (input ("Enter number: "))
    if n > 1:
        break

for n in range (1, 20):
    # main program
    a = 2*n
    b = (n**2)-1
    c = (n**2)+ 1
    PT = [a, b, c]
    PT.sort()

    # printing output
    print (f"\n-> {PT[0]}\u00b2 + {PT[1]}\u00b2 = {PT[2]}\u00b2")
    print (f"-> {(PT[0])**2} + {(PT[1])**2} = {(PT[2])**2}")
    print (f"::: Hence, Pythagorean Triplet --> ({PT[0]}, {PT[1]}, {PT[2]})")

    print ('*'*width)  # Finishing line