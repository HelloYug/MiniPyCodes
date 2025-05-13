code = {"1" : "A", "2" : "B",
        "3" : "C", "4" : "D",
        "5" : "E", "6" : "F",
        "7" : "G", "8" : "H",
        "9" : "I", "10" : "J",
        "11" : "K", "12" : "L",
        "13" : "M", "14" : "N",
        "15" : "O", "16" : "P",
        "17" : "Q", "18" : "R",
        "19" : "S", "20" : "T",
        "21" : "U", "22" : "V",
        "23" : "W", "24" : "X",
        "25" : "Y", "26" : "Z"}

#input
phnum= input ("Enter number: ")

#removing spaces
ok = ""
for char in phnum:
    if char != " ":
        ok += char
phnum = ok

#checking if integer or not
while True:
    try:
       agnum= int (phnum)
       if type (agnum) == int:
           break
    except ValueError:
        print ("\nEnter a Valid Number!")
        phnum= input ("Enter number: ")

print ("Number to be Encrypted: ", phnum)

#main program
absnum= abs (agnum**2)
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
    
#printing final output
print ("\nEncrypted number: ", txt)
