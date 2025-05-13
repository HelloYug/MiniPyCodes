#Yug's TXT DATA file Decrypter
#other info
width=50

#heading
print ("-" * width)
print (("- Yug's Python Text Decrypter -").center(width))
print ("-" * width)

#password Protection
print ((" THE FILE IS PASSWORD PROTECTED ").center(width,"-"))
username = input ("Enter your username: ")
pwd = input ("Enter your password: ")

count = 0
while (username != "yugla") or (pwd != "1608"):
        print (("Either username or password mismatched").center (width,"-"))
        count += 1
        username = input("Enter your username: ")
        pwd = input ("Enter your password: ")
        
        if (username == "yugla") and (pwd == "1608"):
                continue
        
        if count == 1:
                print ((" Intruders not Allowed ").center(width,"-"))
                print ((" WARNING! "*3).center(width,"-"))
                print ((" Just Get Out! ").center(width,"-"))
                break
        
else:
        print ("\tlogging in...")
        print ("*"*width)

        #input
        string = input ("Enter Text: ")
        print ("Text to be Decrypted:", string)

        #Removing extra characters
        string1 = ""
        for i in string:
            if i != "^":
                string1 += i
                
        string2 = ""        
        for j in string1:
            if j != "$":
                string2 += j
                
            #print ("Removed characters:", string2)

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
            
            #print ("Randomized sentence:", "".join (encrypttorandomised))

        #removing random characters
        for i in range (2, len(encrypttorandomised), 2):
            try:
                del encrypttorandomised[i]
            except IndexError:
                pass

        #joining to form unrandomised sentence
        unrandomizedtext = "".join(encrypttorandomised)
            #print ("Unrandomized text:", unrandomizedtext)

        #removing last space
        if unrandomizedtext[0] == "_":
            uninvertedtext = unrandomizedtext [1:]
        else:
            uninvertedtext = unrandomizedtext

            #print ("uninvertedtext:", uninvertedtext)

        #inverting string to get decrpyted text
        Decrypted_text = uninvertedtext[::-1]

        #printing output
        print ("\nDecrypted text: ", Decrypted_text)