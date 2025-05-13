# Python Functions Library Made by Yug Agarwal
# This module is *NOT* an open Source use module, contact the owner before using.
# Email : yugagarwal704@gmail.com
# Phone : +91 7011403558

# List of Functions present in list
    # 1.  heading --> To write Document headings
    # 2.  locking --> Locking System in a Code
    # 3.  InputData --> Asks for input till getting desired datatype
    # 4.  AniType --> prints the text in typewritter effect.
    # 5.  DeciRange --> Returns a list of values of the range with step value as integer and float. Works exactly like range function but with float values as well.
    # 6.  YTDownloader --> YouTube Video Downloader.
    # 7.  RandDeci --> Gives a random decimal value between the given range.

    # 8. Formatter --> String and Number Formatting Features and functions.
        # 01. StringListAD --> On every difference of character type in alphabet or digit, it is added to a list.
        # 02. StringListAll --> On every difference of character type in alphabet or digit or character, it is added to a list.
        # 03. FormatNum --> Returns number with trailing zeros as string.
        # 04. DeciFormatNum --> Returns the number given formatted with trailing and following zeros as string.
        # 05. DeciIntFormatter --> returns the number in integer datatype if its an integer otherwise if an float returns as float.
        # 06. GetInitials -->  Returns the given name in short form.
        # 07. RandomShuffle -->  Shuffles the data in the given data (either string, list, tuple, dictionary) and returns in the same datatype.

    # 9. DataManagement --> This class offers functions using which you Encrypt or Decrypt any text or number given.
        # 01. CharNum --> Returns the number in series of the string/word passed in integer type.
        # 02. NumChar --> Returns the string/alpha code in series of the integer passed in string datatype in uppercase.
        # 03. NumEncryption --> Returns the number into a encrypted form in string datatype in uppercase.
        # 04. NumDecryption --> Returns the orignal number which was encrypted using NumEncryption() in integer datatype.
        # 05. Encryption --> Encrypts the given string into an unreadable format.
        # 06. Decryption --> Decrypts the given string into an readable format which was encrypted by Encryption().

    # 10. TurtleShapes --> Makes Shapes in Python Turtle Drawing window.
        # 01. square --> Draws a square in Python Turtle Drawing window.
        # 02. triangle --> Draws a triangle in Python Turtle Drawing window.
        # 03. hexagon --> Draws a hexagon in Python Turtle Drawing window.
        # 04. polygon --> Draws a polygon with N number of sides in Python Turtle Drawing window.

    # 11. Lines --> Prints a lines of a particular character.
        # 01. starline --> Prints "*" N times.
        # 02. minusline --> Prints "-" N times.
        # 03. appline --> Prints "~" N times.
        # 04. MyLine --> Prints "<Provided Character>" N times.

    # 12. Maths --> Mathematical functions
        # 01. GCD --> Calculates Greatest Common Factor of the given data list.
        # 02. LCM --> Calculates Least Common Multiple of the given data list.
        # 03. DecimalToFraction -->  Converts the given number value into fraction.

    # 13. Sales --> Amount calculation functions
        # 01. SuccessiveDiscount --> Calculates Successive discounts on a given amount.

    # 00.  class YugInfo --> All the information related to Yug Agarwal.


# -------------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------ Individual Functions ------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------
def heading(L, Top_Line, Bottom_Line, width):
    '''
    Heading Function;\n
    \tL --> Provide a list of headings you want to print
    \tHeadline --> Top line (as string)\n
    \tendline --> bottom line (as string)\n
    \twidth --> heading width\n\n

    Formatting;\n
    \theadline*width\n
    \t\tL1.center(width)\n
    \t\tL2.center(width)\n
    \tendline*width
    '''
    print (Top_Line*width)
    for i in L:
        print ((i).center(width))
    print (Bottom_Line*width)

# 02 --------------------------------------------------------------------------------------------------------------------------------------------
def locking(TryTimes, width, Username = "yugla", Password = "1608"):
    '''
    ***Use this to copy the code, not to use as function***\n
    Argumnets Info;\n
    \tTryTimes --> This is the maximum no. of times you get to enter the username and id\n
    \twidth --> width for heading\n
    \tUsername --> Enter Username for the protection (Default: "yugla")\n
    \tPassword --> Enter Password for the protection (Default: "1608")\n\n

    If no. of times exceeds TryTimes the Python Script is exited.
    '''

    print ((" THE FILE IS PASSWORD PROTECTED ").center(width,"-"))
    UsernameInput = input("Enter your username: ")
    PasswordInput = eval (input ("Enter your password: "))

    count=0
    while (UsernameInput != Username) or (PasswordInput != Password):
        print (("Either username or password mismatched").center (width,"-"))
        count += 1
        UsernameInput = input("Enter your username: ")
        PasswordInput = input ("Enter your password: ")
        
        if (UsernameInput == Username) and (PasswordInput == Password):
            break
        
        elif count == TryTimes:
            print ((" Intruders not Allowed ").center(width,"-"))
            print ((" WARNING! "*3).center(width,"-"))
            print ((" Just Get Out! ").center(width,"-"))
            from sys import exit
            exit()

    print ("\tlogging in...")
    print ("*"*width)

# 03 --------------------------------------------------------------------------------------------------------------------------------------------
def InputData(ToVerify, DataType, ErrorType, AskTimes, ErrorMessage = "\nEnter a Valid input!", ErrorCaseInput = "Enter data: "):
    '''
    ***Use this to copy the code, not to use as function***\n\n

    This function asks for Input till it gets desired type of input.\n
    returns the data in desired datatype or will asked for \n\n
    \n
    Arguments Info;\n
    \tToVerify --> Input to get of desired datatype.\n
    \tDataType --> Desired Data Type of input.\n
    \tErrorType --> ErrorType faced while getting desired datatype.\n
    \tAskTimes --> This no. of times system will ask for input if desired datatype not found.\n
    \tErrorMessage --> If desired datatype not found this message will me shown as errormessage. (Default: \\nEnter a Valid input!)\n
    \tErrorCaseInput --> If desired datatype not found the input asked message will be this. (Default: Enter data: )
    '''
    
    cnt = 0
    while True:
        try:
            DataType (RepeatToVerify)
            if type (ToVerify) == DataType:
                break
            
        except ErrorType:
            print (ErrorMessage)
            RepeatToVerify = input (ErrorCaseInput)

        if cnt == AskTimes:
            break

        cnt += 1

    return RepeatToVerify

# 04 --------------------------------------------------------------------------------------------------------------------------------------------
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
            
# 05 --------------------------------------------------------------------------------------------------------------------------------------------
def DeciRange (a, b, Gap):
    '''
    Returns a list of values of the range with step value as integer and float.\n
    Works exactly like range function but with float values as well.\n
    Does not include upper limit.\n\n

    Arguments info;\n
    \ta --> start value\n
    \tb --> end value
    \tGap --> step value (can be decimal)\n\n
    
    Example;\n
    \tFunc(2, 3, 0.25) --> [2.0, 2.25, 2.5, 2.75]\n
    \tFunc(2, 3, 0.2) --> [2.0, 2.2, 2.4, 2.6, 2.8]\n
    \tFunc(2, 10, 2) --> [2.0, 4.0, 6.0, 8.0]
    '''

    # Finding the no. of digit to round of
    cnt = 0
    l = len (str (Gap))
    for i in str (Gap):
        if i == ".":
            break
        cnt += 1
    rou = l - cnt
    
    # Converting values to Float type
    a, b, Gap = float (a), float (b), float (Gap)
    Final =[]

    # Creating a list of values
    while a < b:
        print (round(a, rou))
        Final.append(round (a, rou))
        a += Gap

    flag = b
    if Gap < 0:
        flag = a
        
    # Handling a error
    if Final[-1] == flag:
        Final.remove(b)

    # Returning final list
    return Final  

# 06 --------------------------------------------------------------------------------------------------------------------------------------------        
def YTDownloader(link):
    '''
    ***YouTube Video Downloader***\n
    Argument Info --> link --> recieves the link or URL address of the video to be downloaded
    '''
    from pytube import YouTube
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download()


# 07 --------------------------------------------------------------------------------------------------------------------------------------------
def RandDeci(Start, End, DecimalDigit = 1):
    '''
    Return random Decimal in range [Start, End], including both end points upto n number of DecimalDigit.\n
    Example;\n
    \tFunc(5, 19, 4) --> 13.5869\n
    \tFunc(11, 12, 1) --> 11.3
    '''

    from random import randint
    x = str(randint(int(Start), int(End)))
    y = "."
    for i in range (int (DecimalDigit)):
        a = str(randint (0, 9))
        y += a

    num = float (x+y)
    if num > int(End):
        num -= 1

    return num 

# 08 --------------------------------------------------------------------------------------------------------------------------------------------    
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------- Formatter ------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------    
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
    
# 02 --------------------------------------------------------------------------------------------------------------------------------------------
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

# 03 --------------------------------------------------------------------------------------------------------------------------------------------
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

# 04 --------------------------------------------------------------------------------------------------------------------------------------------
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

# 05 --------------------------------------------------------------------------------------------------------------------------------------------
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

# 06 --------------------------------------------------------------------------------------------------------------------------------------------
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

# 07 --------------------------------------------------------------------------------------------------------------------------------------------
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


# 09 --------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''-------------------------------------------------------------- Data Management ---------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------
def CharNum(string):
    '''
    *** Recieves one word at a time ***\n
    Returns the number in series of the string/word passed in integer datatype.\n
    Argument info --> string --> The word to get number in series of.\n
    Example;\n
    "a" --> 1, "z" --> 26, "ac" --> 29\n
    \tFunc("yug") --> 17453\n
    \tFunc("Four") --> 116160
    '''

    # Defining Dictionary
    Dictionary = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}

    l = list (string.upper())
    s = Dictionary.get (l [0])

    for i in range (1, len (l)):
        p = s * 26
        s = p + Dictionary.get (l[i])
        
    return (s)

# 02 --------------------------------------------------------------------------------------------------------------------------------------------
def NumChar(number):
    '''
    ***Recieves one word at a time***\n
    Returns the string/alpha code in series of the integer passed in string datatype in uppercase.\n
    Argument info --> number --> The integer to get string in series of.\n
    Example;\n
    1 --> "A", 26 --> "Z", 30 --> "AD"\n
    \tFunc(17453) --> "YUG"\n
    \tFunc(116160) --> "FOUR"
    '''

    # Defining dictionary
    Dictionary = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 14 : "N", 15 : "O", 16 : "P", 17 : "Q", 18 : "R", 19 : "S", 20 : "T", 21 : "U", 22 : "V", 23 : "W", 24 : "X", 25 : "Y", 26 : "Z"}

    # Main program
    op = ""
    flag = 0

    if number % 26 == 0:
        number -= 1
        flag = 1

    while True:
        try:
            op += Dictionary.get (number%26)
            number //= 26

        except TypeError:
            break

    op = (list(op))[::-1]
    if flag == 1:
        op[-1] = "Z"
        op = "".join (op)
        
    return op

# 03 --------------------------------------------------------------------------------------------------------------------------------------------
def NumEncryption(number):
    '''
    ***Pass integer only***\n
    Returns the number into a encrypted form in string datatype in uppercase.\n
    Argument info --> number --> pass the integer or the number you want to encrypt.\n
    Example;\n
    \tFunc(52) --> "EB"\n
    \tFunc(258) --> "YH"
    '''

    code = {"1" : "A", "2" : "B", "3" : "C", "4" : "D",
        "5" : "E", "6" : "F", "7" : "G", "8" : "H",
        "9" : "I", "10" : "J", "11" : "K", "12" : "L",
        "13" : "M", "14" : "N", "15" : "O", "16" : "P",
        "17" : "Q", "18" : "R", "19" : "S", "20" : "T",
        "21" : "U", "22" : "V", "23" : "W", "24" : "X",
        "25" : "Y", "26" : "Z"}

    # main program
    absnum= abs (number**2)
    strnum = str (absnum)
    txt = ""
    count = 0

    for i in range (len (strnum)):
        try:
            numnum = int (strnum [i + count])
            if numnum <= 2:

                if numnum == 0:
                    txt += "0"

                else:
                    val = int (str (numnum) + str (strnum[i+1+count]))

                    if val <= 26:
                        count += 1
                        keyto = str (val)
                        txt += code.get (keyto)

                    else:
                        keyto = str (numnum)
                        txt += code.get (keyto)                        

            else:
                keyto = str (numnum)
                txt += code.get (keyto)                    

        except IndexError:
            if count + i == len (strnum) - 1:
                keyto =  strnum [-1]
                txt += code.get (keyto)
                break

            else:
                pass
        
    # returning final output
    return txt

# 04 --------------------------------------------------------------------------------------------------------------------------------------------
def NumDecryption(Encrypted_Number_String):
    '''
    ***Pass String only (Non Case Sensitive)***\n
    Returns the orignal number which was encrypted using NumEncryption() in integer datatype.\n
    Argument info --> Encrypted_Number_String --> pass the string you want to decrypt.\n
    Example;\n
    \tFunc("EB") --> 52\n
    \tFunc("YH") --> 258\n
    \tFunc("s0K") --> 19011
    '''

    code = {"A" : "1", "B" : "2",
        "C" : "3", "D" : "4",
        "E" : "5", "F" : "6",
        "G" : "7", "H" : "8",
        "I" : "9", "J" : "10",
        "K" : "11", "L" : "12",
        "M" : "13", "N" : "14",
        "O" : "15", "P" : "16",
        "Q" : "17", "R" : "18",
        "S" : "19", "T" : "20",
        "U" : "21", "V" : "22",
        "W" : "23", "X" : "24",
        "Y" : "25", "Z" : "26"}

    string = Encrypted_Number_String.upper ()
    string = string.strip ()
    fstring = ""

    for char in string:
        if char == "0":
            fstring += "0"

        if char == " ":
            fstring += ""
            
        if not char.isdigit() and char.isalpha():
            fstring += char

    #Decrypting number
    txt = ""
    for char in fstring:
        if char == "0":
            txt += "0"

        if char == " ":
            txt += " "

        else:
            if char != "0":
                txt += code.get (char)


    number = int ((int (txt))**0.5)

    # returning output
    return number

# 05 --------------------------------------------------------------------------------------------------------------------------------------------
def Encryption(string):
    '''
    Encrypts the given string into an unreadable format.\n
    returns the encrypted data in string datatype.\n
    Argument info --> string --> pass the string you want to encrypt.\n
    Example,\n
    \tFunc("Hello World") --> "d$$_lrCrW^o )${ol^le*^}H"\n
    \tFunc("Jai mata di!") --> "i!$dy$} ta$^a/^-mi^ au<J"
    '''

    string = string.strip()
    
    #string formatting
    if (len(string)%2) == 1:
            string += "_"

    #inverted sentence
    invertedsentence = string[::-1]
    
    #Adding random character after every 2 characters
    from random import choice
    from string import ascii_letters, digits, punctuation
    listofyugmix = list (ascii_letters + digits + punctuation)
    listofyugmix.remove ("_" and "^" and "$")

    randomizedsentence = ""
    for i in range(0, len(invertedsentence), 2):                 
            char = str (choice(listofyugmix))
            randomizedadding = invertedsentence[i:i + 2]+ char
            randomizedsentence += randomizedadding
    
    #encrypter cross
    initialindex = 1
    lrs = len (randomizedsentence)
    Encryptedlist = []
    for j in range (int (lrs/2)):
            try:
                    Encryptedlist.append (randomizedsentence[initialindex])
                    initialindex -= 1
                    Encryptedlist.append (randomizedsentence[initialindex])
                    initialindex += 3

            except IndexError:
                    pass
    
    if lrs%2 == 1:
            Encryptedlist.append (randomizedsentence[-1])

    #random insertion of character
    lambai = len (Encryptedlist)
    from random import randint
    for k in range (lambai//5):
            index = randint (0, lambai-1)
            index2 = randint (0, lambai-1)
            Encryptedlist.insert (index, "^")
            Encryptedlist.insert (index2, "$")

    #concatenating to get Encrypted text
    Encrypted_text = "".join(Encryptedlist) #finalresult

    # returning Output
    return Encrypted_text

# 06 --------------------------------------------------------------------------------------------------------------------------------------------
def Decryption (string):
    '''
    Decrypts the given string into an readable format which was encrypted by Encryption().\n
    returns the decrypted data in string datatype.\n
    Argument info --> string --> pass the string you want to decrypt.\n
    Example,\n
    \tFunc("d$$_lrCrW^o )${ol^le*^}H") --> "Hello World"\n
    \tFunc("i!$dy$} ta$^a/^-mi^ au<J") --> "Jai mata di"
    '''

    #Removing extra characters
    string1 = ""
    for i in string:
        if i != "^":
            string1 += i
            
    string2 = ""        
    for j in string1:
        if j != "$":
            string2 += j
            
    #Encryption cross to Randomized sentence
    if len(string2)%2 == 1:
        alpha = str (string2[-1])
        string3 = string2[:len (string2)-1]
        
    else:
        string3 = string2

    initialindex = 1
    encrypttorandomised = []

    for k in range (int (len(string3)/2)):
                    encrypttorandomised.append (string3[initialindex])
                    initialindex -= 1
                    encrypttorandomised.append (string3[initialindex])
                    initialindex += 3

    if len(string2)%2 == 1:
        encrypttorandomised.append (alpha)

    #removing random characters
    for i in range (2, len(encrypttorandomised), 2):
        try:
            del encrypttorandomised[i]
        except IndexError:
# 0 ----------------------------------------------------------------------------------------------------------------------------------------
            pass

    #joining to form unrandomised sentence
    unrandomizedtext = "".join(encrypttorandomised)

    #removing last space
    if unrandomizedtext[0] == "_":
        uninvertedtext = unrandomizedtext [1:]
    else:
        uninvertedtext = unrandomizedtext

    #inverting string to get decrpyted text
    Decrypted_text = uninvertedtext[::-1]

    # return output
    return Decrypted_text


# 10 --------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''--------------------------------------------------------------- Turtle Shapes ----------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------
def square(SideLength):
    '''
    Draws a square in Python Turtle Drawing window.\n
    Arguments Info;\n
    \tSideLength --> recieves the length of the side of the polygon formed\n
    '''

    from turtle import Turtle
    t = Turtle()
    for i in range (4):
        t.fd (SideLength)
        t.right (90)

# 02 --------------------------------------------------------------------------------------------------------------------------------------------
def triangle (SideLength):
    '''
    Draws a triangle in Python Turtle Drawing window.\n
    Arguments Info;\n
    \tSideLength --> recieves the length of the side of the polygon formed\n
    '''
    
    from turtle import Turtle
    t = Turtle()
    for i in range (3):
        t.fd (SideLength)
        t.right (120)

# 03 --------------------------------------------------------------------------------------------------------------------------------------------
def hexagon (SideLength):
    '''
    Draws a hexagon in Python Turtle Drawing window.\n
    Arguments Info;\n
    \tSideLength --> recieves the length of the side of the polygon formed\n
    '''

    from turtle import Turtle
    t = Turtle()
    for i in range (6):
        t.fd (SideLength)
        t.right (60)

# 04 --------------------------------------------------------------------------------------------------------------------------------------------
def polygon (SideLength, NoOfSides):
    '''
    Draws a polygon with N number of sides in Python Turtle Drawing window.\n
    Arguments Info;\n
    \tSideLength --> recieves the length of the side of the polygon formed\n
    \tNoOfSides --> recieves the number of sides polygon drawn should have (Minimum: 3 --> triangle)\n
    '''

    if NoOfSides < 3:
        return "Error: Number of sides less than 3, inefficient to make a polygon"
        
    else:
        ang = 360/NoOfSides
        from turtle import Turtle
        t = Turtle()
        for i in range (NoOfSides):
            t.fd (SideLength)
            t.right (ang)    


# 11 --------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------- Lines --------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------
def starline (PrintTimes):
    '''
    PrintTimes --> prints "*" this times
    '''
    print ("*" * PrintTimes)

# 02 --------------------------------------------------------------------------------------------------------------------------------------------
def minusline (PrintTimes):
    '''
    PrintTimes --> prints "-" this times
    '''
    print ("-" * PrintTimes)

# 03 --------------------------------------------------------------------------------------------------------------------------------------------
def appline(PrintTimes):
    '''
    PrintTimes --> prints "~" this times
    '''
    print ("~" * PrintTimes)

# 04 --------------------------------------------------------------------------------------------------------------------------------------------
def Myline (Character, PrintTimes):
    '''
    Character --> The character to be printed\n
    PrintTimes --> prints Character this times
    '''
    print (Character * PrintTimes)

# 12 --------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------- Maths --------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------
def GCD (nums):
    '''
    Returns the Greatest Common Divisor as integer of the given list as nums and a nested list of all divisors of each number in the given list.\n
    nums --> list of numbers to find GCD of.\n
    returns a tuple --> (GCD, Nested list of factors of each number in sortrd given list)\n
    Example;\n
    \tFunc([10, 25, 20]) --> (5, [[1, 2, 5, 10],[1, 2, 4, 5, 10, 20],[1, 5, 25]])\n
    \tFunc([7, 20, 21]) --> (1, [[1, 7],[1, 2, 4, 5, 10, 20], [1, 3, 7, 21]])
    '''

    nums.sort()
    # Finding multiples
    listnums = []
    for GCD in nums:
        NumL = [1]

        for k in range (2, GCD+1):
            if GCD%k == 0:
                NumL.append (k)

        listnums.append (NumL)

    # making list of no. of multiples
    lennums = []
    for GCD in listnums:
        lennums.append (len (GCD))

    # Finding list with least elements and reversing it
    SmallIndexList = listnums [(lennums.index (min (lennums)))]
    SmallIndexListReverse = SmallIndexList[::-1]

    # Finding GCD
    for GCD in SmallIndexListReverse:
        cnt = 0
            
        for j in listnums:
            if GCD not in j:
                break

            cnt += 1
        
        if cnt == len(nums):
            break

    # returning output
    return GCD, listnums

# 02 --------------------------------------------------------------------------------------------------------------------------------------------
def LCM (nums):
    '''
    Returns the Least Common Multiple as integer of the given list as nums and a nested list of all multiples of each number is given list upto LCM.\n
    nums --> list of numbers to find LCM of.\n
    returns a tuple --> (LCM, Nested list of multiples of each number in sortrd given list)\n
    Example;\n
    \tFunc([3, 5]) --> (15, [[3, 6, 9, 12, 15], [5, 10, 15]])\n
    \tFunc([15, 10, 20]) --> (60, [[10, 20, 30, 40, 50, 60], [15, 30, 45, 60], [20, 40, 60]])
    '''

    nums.sort()
    lcm = max (nums) # Fixing largest number as LCM for instance

    # Finding LCM
    while True:
        TempList = []
        for i in nums:
            TempList.append (lcm % i)
        
        flag = 1
        for i in TempList:
            if i != 0:
                flag = 0
                lcm += 1
                break

        if flag == 1:
            break

    # creating a list of all multiples till LCM
    AllMultiplesList = []
    for i in nums:
        MutliplesList= [i]
        digit = lcm//i

        for j in range (2, digit+1):
            MutliplesList.append (i*j)

        AllMultiplesList.append (MutliplesList)

    # returning Output
    return lcm, AllMultiplesList

# 03 --------------------------------------------------------------------------------------------------------------------------------------------
def DecimalToFraction(Value):
    '''
    *** Pass Decimal or integer value only or face ValueError ***\n
    It returns the provided value into least reduced fraction form in string datatype.\n
    Parameter info; Value --> Float or integer value that needs to be converted into fraction\n
    Example;\n
    \tFunc(0.25) --> "1/4"\n
    \tFunc(2.52) --> "63/25"\n
    \tFunc(5.500) --> "11/2"\n
    \tFunc(6) --> "6/1"
    '''
    
    if (type(Value) == float) or (type(Value) == int):
        try:
            StrV = str (float (Value))
        except ValueError:
            pass

        # finding decimal place
        count = 0
        for i in StrV[::-1]:
            if i == ".":
                forward = int (StrV[StrV.index(".")+1:])
                break
            count += 1

        if forward != 0:
            # converting decimal to integer
            expo = 10**count
            if type (Value) != int:
                FullX = int (Value * expo)

            # provinding list of prime numbers to check for divisibility
            prime = [2,3,5,7,11,13,17,19,23,29,31,37,41]

            # main program (find least reduced fraction)
            frac = [FullX, expo]
            while True:
                flag = 0
                for i in prime:
                    if (frac[0]%i == 0) and (frac[1]%i == 0):
                        frac[0] = int(frac[0]/i)
                        frac[1] = int(frac[1]/i)
                        flag = 1
                        break

                if flag == 0:
                    break

            return f"{frac[0]} / {frac[1]}"

        else:
            return f"{Value} / 1"

    else:
        raise ValueError ("The argument is not a number!!!")

# 13 --------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------- Sales --------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 01 --------------------------------------------------------------------------------------------------------------------------------------------
def SuccessiveDiscount (DiscountList, Amount):
    '''
    Returns a tuple: (Total Discount Percent, Price After Discount, Discounted Amount).\n
    DiscountList --> Provide a list of the successive amount percentages.\n
    Amount --> Provide the amount on which the discount is to be calculated.\n
    Example;\n
    \tFunc([20, 25], 200) --> (40.0, 120.0, 80)
    \tFunc([8, 6, 2], 250) --> (15.25, 211.88, 38)
    '''
    s = 100
    for i in DiscountList:
        s -= i*s/100

    TotalDiscountPercent = round (100 - s, 2)
    PriceAfterDiscount = round (Amount * s / 100, 2)
    DiscountedAmount = round (Amount - PriceAfterDiscount)

    return TotalDiscountPercent, PriceAfterDiscount, DiscountedAmount

# 00 --------------------------------------------------------------------------------------------------------------------------------------------
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------ Yug Info ------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
# 00 --------------------------------------------------------------------------------------------------------------------------------------------
class YugInfo:
    def name(type):
        if type == "full":
            return "Yug Agarwal"
        if type == "first":
            return "Yug"
        if type == "last":
            return "Agarwal"

    def age():
        return "16"

    class school:
        def Grade(type):
            if type == "class":
                return "11"
            if type == "sec":
                return "A"

    def PhoneNo(Relation):
        if Relation == "self":
            return "7011403558"
        if Relation == "mother":
            return "9312027122"
        if Relation == "father":
            return "9312127122"
        if Relation == "work":
            return "9643433354"

    def SchoolName(time):
        if time == "now":
            return "Bhai Parmanand Vidya Mandir, Surya Niketan"
        if time == "previous":
            return "New Oxford Public School, Vivek Vihar"

    def address():
            return "Flat No.704 , Tower 1, Parsvnath Regalia, 149, Grand Trunk Road, Sahibabad-201005, Ghaziabad, Uttar Pradesh (India)"

    def Email(Relation):
        if Relation == "self":
            return "yugagarwal704@gmail.com"
        if Relation == "mother":
            return "shaliniagarwal67717@gmail.com"
        if Relation == "father":
            return "sanjaymedipol@gmail.com"
        if Relation == "work":
            return "yugindustries21@gmail.com"


'''--------------------------------------------------------------------------------------------------------------------------------------------''' # ------------------
'''--------------------------------------------------------------------------------------------------------------------------------------------''' # ------------------


# class TurtleShapes:
    # '''
    # Makes Shapes in Python Turtle Drawing window in Clock - Wise Direction.\n\n

    # Functions listed;\n
    # \ttriangle --> polygon of three sides\n
    # \tsquare --> polygon of four sides\n
    # \thexagon --> polygon of six sides\n
    # \tpolygon --> polygon of N number of sides\n\n

    # This Class functions take two below listed arguments;\n
    # \tSideLength --> recieves the length of the side of the polygon formed\n
    # \tFor polygon(); NoOfSides --> recieves the number of sides polygon drawn should have
    # '''

# class Formatter:
    # '''
    # This class has formatting features;\n
    # All the functions return string valus\n
    # Functions Listed;\n
    # \tStringListAD --> On every difference of character type in alphabet or digit, it is added to a list.\n
    # \tStringListAll --> On every difference of character type in alphabet or digit or character, it is added to a list.\n
    # \tFormatNum --> Returns number with trailing zeros as string.
    # '''

# class lines:
    # '''
    # prints a lines of a particular character;\n\n

    # Function Name -- Printing Character\n
    # \tstarline ------> "*"\n
    # \tminusline -----> "-"\n
    # \tappline -------> "~"\n
    # \tMyLine  -------> "<Provided Character>"
    # '''

# class DataManagement:
    # '''
    # This class offers functions using which you Encrypt or Decrypt any text or number given.\n
    # Functions available;\n
    # \tCharNum --> Returns the number in series of the string/word passed in integer type.\n
    # \tNumChar --> Returns the string/alpha code in series of the integer passed in string datatype in uppercase.\n
    # \tNumEncryption --> Returns the number into a encrypted form in string datatype in uppercase.\n
    # \tNumDecryption --> Returns the orignal number which was encrypted using NumEncryption() in integer datatype.\n
    # \tEncryption --> Encrypts the given string into an unreadable format.\n
    # \tDecryption --> Decrypts the given string into an readable format which was encrypted by Encryption().
    # '''

