from random import choice, randint
from string import ascii_letters, digits, punctuation

# Code dictionaries for encryption/decryption
code1 = { "A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9", 
          "J": "10", "K": "11", "L": "12", "M": "13", "N": "14", "O": "15", "P": "16", "Q": "17", 
          "R": "18", "S": "19", "T": "20", "U": "21", "V": "22", "W": "23", "X": "24", "Y": "25", "Z": "26"}

code2 = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", 
          "10": "J", "11": "K", "12": "L", "13": "M", "14": "N", "15": "O", "16": "P", "17": "Q", 
          "18": "R", "19": "S", "20": "T", "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y", "26": "Z"}

def NumberDecrypter(string):
    """
    Decrypts a given string of numbers into a number, using a pre-defined code mapping.
    
    Parameters:
        string (str): The string of encrypted numbers to be decrypted.
    
    Returns:
        int: The decrypted number.
    """
    string = string.upper().strip()
    fstring = "".join([char if char.isdigit() or char.isalpha() else '' for char in string])
    
    txt = "".join([code1.get(char, '') for char in fstring])
    number = int(int(txt)**0.5)
    
    return number


def NumberEncrypter(phnum):
    """
    Encrypts a given number using a pre-defined code mapping.
    
    Parameters:
        phnum (str): The number to be encrypted.
    
    Returns:
        str: The encrypted number as a string.
    """
    phnum = "".join([char for char in phnum if char != " "])
    
    while True:
        try:
            agnum = int(phnum)
            break
        except ValueError:
            return "Invalid number input"

    absnum = abs(agnum**2)
    strnum = str(absnum)
    
    txt = ""
    count = 0
    
    for i in range(len(strnum)):
        try:
            numnum = int(strnum[i + count])
            if numnum <= 2:
                if numnum == 0:
                    txt += "0"
                else:
                    val = int(str(numnum) + str(strnum[i + 1 + count]))
                    if val <= 26:
                        count += 1
                        txt += code2.get(str(val), '')
                    else:
                        txt += code2.get(str(numnum), '')
            else:
                txt += code2.get(str(numnum), '')
        except IndexError:
            if count + i == len(strnum) - 1:
                txt += code2.get(str(strnum[-1]), '')
                break
    return txt


def StringEncrypter(d):
    """
    Encrypts a string using random character insertions and reordering.
    
    Parameters:
        d (str): The text to be encrypted.
    
    Returns:
        str: The encrypted text.
    """
    yugmix = ascii_letters + digits + punctuation
    f = list(yugmix)
    for char in ['_', '^', '$']:
        if char in f:
            f.remove(char)
    
    # Padding for odd length
    if len(d) % 2 == 1:
        d += "_"

    # Reverse input
    e = d[::-1]

    # Insert random characters between every 2 letters
    h = "".join([e[i:i + 2] + choice(f) for i in range(0, len(e), 2)])

    # Rearranging characters
    l = 1
    m = len(h)
    if m % 2 == 1:
        m += 1

    n = []
    for j in range(int(m / 2)):
        try:
            n.append(h[l])
            l -= 1
            n.append(h[l])
            l += 3
        except IndexError:
            pass

    if len(h) % 2 == 1:
        n.append(h[-1])

    # Inserting noise characters randomly
    o = len(n)
    for _ in range(o // 5):
        p = randint(0, o - 1)
        q = randint(0, o - 1)
        n.insert(p, "^")
        n.insert(q, "$")

    return "".join(n)


def StringDecrypter(d):
    """
    Decrypts a given string by reversing the encryption process, removing noise characters.
    
    Parameters:
        d (str): The encrypted text to be decrypted.
    
    Returns:
        str: The decrypted text.
    """
    e = "".join([i for i in d if i != "^"])
    f = "".join([j for j in e if j != "$"])

    # Handle odd length by removing the last character if needed
    if len(f) % 2 == 1:
        h = f[-1]
        g = f[:-1]
    else:
        g = f

    # Reordering
    i = 1
    j = []
    for k in range(int(len(g) / 2)):
        j.append(g[i])
        i -= 1
        j.append(g[i])
        i += 3

    if len(f) % 2 == 1:
        j.append(h)

    # Removing extra elements
    for i in range(2, len(j), 2):
        try:
            del j[i]
        except IndexError:
            pass

    # Final output
    k = "".join(j)
    l = k[1:] if k[0] == "_" else k
    m = l[::-1]
    
    return m
