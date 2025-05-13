# permutation and combination Factorial finder
### Making list of the input
def StringList (data):
    # Assigning Empty Variables
    Fstr = ""
    Fdig = ""
    Flist = []

    # Main Function
    for i in data.upper():

        if i.isalpha() == True:
            if Fdig != "":
                Flist.append (Fdig)
                Fdig = ""
            Fstr += i

        else:
            if i.isdigit() == True:
                if Fstr != "":
                    Flist.append (Fstr)
                    Fstr = ""
            Fdig += i

    # To append the last loop
    if Fstr != "":
        Flist.append (Fstr)

    else:
        Flist.append (Fdig)

    # Returning the output
    return Flist

# ### Negetive Integer
# def negetive (num):
#     ShowError = False
#     if num < 0:
#         ShowError = True
        
#     return ShowError

### StringList Conversion
def SLConversion(L):
    for i in L:
        if i.isdigit() == True:
            L[L.index(i)] = int (i)
            # negetive (L[i])
    
    return L

### Factorial Finding
def factorial(n):
    if n == 0:
        return 1
         
    initial = 1
    for i in range (1, n+1):
        initial *= i

    return initial

def combination(N,R):
    return (factorial (N)/(factorial(N-R)*factorial (R)))
    
def permutation (N,R):
    return (factorial (N)/factorial (N-R))

### Front end --------------------------------------------------------
#other info
width = 54

# heading
print ("_"*width)
print (("Permutation, Combination & Factorials").center(width))
print ("¯"*width)

print ("Permutation: 5P2 --> 20\n\t\tCombination: 5C2 --> 10\n\t\t\t\tFactorial: F5 --> 120")
print (("-"*(int (width*0.85))).center(width))

while True:
    # input
    number = input ("Enter the command: ")
    data = SLConversion (StringList (number))
        # print (data)

    # conditioning
    if data[0] == "F":
        OP = factorial (data[1])

    if data [1] == "P":
        OP = permutation (data[0],data[2])

    if data [1] == "C":
        OP = combination (data[0],data[2])

    # printing output
    print (f"Output: {int(OP)}")
    print ("_"*width)

