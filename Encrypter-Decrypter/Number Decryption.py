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
#other info
width = 50
#heading
print ("*"*width)
print (("Number Decrypter").center(width))
print ("*"*width)

#input and string formatting
string = input ("Enter the Encrypted number: ")
string = string.upper ()
string = string.strip ()
fstring = ""

for char in string:
    if char == "0":
        fstring += "0"

    if char == " ":
        fstring += ""
        
    if not char.isdigit() and char.isalpha():
        fstring += char

print ("Number to be Decrypted: ", fstring)

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
print ("\nDecrypted number:", number)
