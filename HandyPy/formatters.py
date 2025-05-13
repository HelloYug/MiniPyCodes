# AniType --> prints the text in typewritter effect.
# StringListAD --> On every difference of character type in alphabet or digit, it is added to a list.
# StringListAll --> On every difference of character type in alphabet or digit or character, it is added to a list.
# FormatNum --> Returns number with trailing zeros as string.
# DeciFormatNum --> Returns the number given formatted with trailing and following zeros as string.
# DeciIntFormatter --> returns the number in integer datatype if its an integer otherwise if an float returns as float.
# GetInitials -->  Returns the given name in short form.
# ShuffleData -->  Shuffles the data in the given data (either string, list, tuple, dictionary) and returns in the same datatype.

def AniType (text, THFNC = 0.03, THFNL = 0.25):
    '''
    prints the text in typewritter effect.\n
    arguments info;\n
    \ttext --> recives string which is to be printed in typewritter effect\n
    \tTHFNC --> time halt for next character (Default: 0.03 (s))\n
    \tTHFNL --> time halt for next line (Default: 0.25 (s))
    '''

    # import time   
    from time import sleep 
    for char in text:
        print (char, end = "")

        # pausing condition
        if char == " ":
            pass
        elif char!="\n":
            sleep (THFNL)
        else:
            sleep (THFNC)

def StringListAD (string):
    '''
    StringListAD --> String List A(Alphabets) D(Digits)\n
    Returns a list of formatted string.\n
    On every difference of character type in alphabet or digit, it is added to a list.\n
    Argument info --> data --> Enter the string you want to get formatted.\n
    Example;\n
    \t--> Func("AG52 89j k 04") --> ['AG', '52 89', ' ', 'JK', ' 04']\n
    \t--> Func("AG52 89j k? &y /04") --> ['AG', '52 89', ' ', '? &', 'JKY', ' /04']
    '''

    # Assigning Empty Variables
    Fstr = ""
    Fdig = ""
    Flist = []

    # Main Function
    for i in string:

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
    
def StringListAll (string):
    '''
    StringListAll --> String List All (Characters, Digits and Alphabets)\n
    Returns a list of formatted string.\n
    On every difference of character type in alphabet or digit or character, it is added to a list.\n
    Argument info --> data --> Enter the string you want to get formatted.\n
    Example;\n
    \t--> Func("AG52 89j k 04") --> ['AG', '52', ' ', '89', 'J', ' ', 'K', ' ', '04']\n
    \t--> Func("AG52 89j k? &y /04") --> ['AG', '52', ' ', '89', 'J', ' ', 'K', '? &', 'Y', ' /', '04']  
    '''

    # Assigning Empty Variables
    Fstr = ""
    Fchar = ""
    Fdig = ""
    Flist = []

    # Main Function
    for i in string:

        if i.isalpha() == True:

            if Fchar != "":
                Flist.append (Fchar)
                Fchar = ""

            if Fdig != "":
                Flist.append (Fdig)
                Fdig = ""

            Fstr += i

        elif i.isdigit() == True:

            if Fstr != "":
                Flist.append (Fstr)
                Fstr = ""

            if Fchar != "":
                Flist.append (Fchar)
                Fchar = ""

            Fdig += i
                    
        else:

            if Fstr != "":
                Flist.append (Fstr)
                Fstr = ""

            if Fdig != "":
                Flist.append (Fdig)
                Fdig = ""

            Fchar += i

    # To append the last loop
    if Fchar != "":
        Flist.append (Fchar)

    elif Fstr != "":
        Flist.append (Fstr)

    else:
        Flist.append (Fdig)

    # Returning the output
    return Flist

def FormatNum(Number, DigitsNum):
    '''
    Returns the number given formatted with trailing zeros.\n
    Return Type --> String\n\n

    Number --> Provide the number to format\n
    DigitsNum --> Number of digits to format the given number into\n\n
    Examples;\n
    \tFunc(5, 2) --> returns "05"\n
    \tFunc(4, 3) --> returns "004"\n
    \tFunc(25, 2) --> returns "25"
    '''
    strNum = str (Number)

    if len(strNum) < DigitsNum:
        zeros = DigitsNum - len (strNum)
        return (("0"*zeros) + strNum)

    return Number      

def DeciFormatNum (Value, IntValue, DeciValue):
    '''
    Returns the number given formatted with trailing and following zeros.\n
    Return Type --> String\n\n

    Value --> Provide the Number to format\n
    IntValue --> Number of digits to format the Integer number with trailing zeros.\n
    DeciValue --> Number of digits to format after decimal point or number of following zeros.\n\n
    Examples;\n
    \tFunc(5, 2, 3) --> returns "05.000"\n
    \tFunc(4.02, 2, 1) --> returns "04.02"\n
    \tFunc("25.1", 3, 4) --> returns "025.1000"
    '''

    Value = str (float (Value)).split(".")

    Integer = Value[0]
    if len(Integer) < IntValue:
        zeros = IntValue - len (Integer)
        Value[0] = (("0"*zeros) + Integer)

    Decimal = Value[1]
    if len(Decimal) < DeciValue:
        zeros = DeciValue - len (Decimal)
        Value[1] = (Decimal + ("0"*zeros))

    return (f"{Value[0]}.{Value[1]}")

def DeciIntFormatter(number):
    '''
    returns the number in integer datatype if its an integer otherwise if an float returns as float.\n
    Example;\n
    \tFunc(3) --> 3 (int)\n
    \tFunc(2.7) --> 2.7 (float)\n
    \tFunc(2.0) --> 2 (int)\n
    \tFunc(4.0068) --> 4.0068 (float)\n
    '''

    numb = str(float (number)).split(".")
    for i in range (1, 10):
        if str(i) in numb[1]:
            return float (number)
    print (type(number)) 
    print ((number))
    return int (number)

def GetInitials(fullname):
    '''
    Returns the given name in short form in string datatype.\n
    Example;\n
    \tFunc("yug agarwal") --> "Y. Agarwal"\n
    \tFunc("Shwetendu sharad Dhanuka") --> "S.S. Dhanuka"
    '''
    NameList = fullname.split()
    ShortName = ""
    for i in range (len(NameList) - 1):
        char = NameList[i]

        if char.isupper() == True:
            ShortName += char + " "
        
        else:
            ShortName += char[0].upper() + "."
    
    return ShortName + " " + NameList[-1].title()

def ShuffleData (data):
    '''
    returns the data in random order in the same data type.\n
    Example;\n
    \tFunc("python") --> "othnyp" | # string\n
    \tFunc([1, 2, 3, 4]) --> [3, 1, 2, 4] | # list\n
    \tFunc((1, 2, 3, 4)) --> (3, 1, 2, 4) | # tuple\n    
    \tFunc({1:2, 3:4, 5:6}) --> {3:4, 1:2, 5:6} | # Dictionary\n
    '''

    from random import choice
    DataType = type (data)
    ChangedData = list (data)
    Length = len (ChangedData)
    L2 = []

    for i in range (Length):
        C = choice (ChangedData)
        L2.append (C)
        ChangedData.remove (C)

    if DataType == str:
        return ("".join(L2))

    elif DataType == dict:
        d = {}
        for i in L2:
            d.update ({i:data[i]})

        return d

    else:
        return (DataType (L2))