# CharNum --> Returns the number in series of the string/word passed in integer type.
# NumChar --> Returns the string/alpha code in series of the integer passed in string datatype in uppercase.
# NumEncryption --> Returns the number into a encrypted form in string datatype in uppercase.
# NumDecryption --> Returns the orignal number which was encrypted using NumEncryption() in integer datatype.
# Encryption --> Encrypts the given string into an unreadable format.
# Decryption --> Decrypts the given string into an readable format which was encrypted by Encryption().


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