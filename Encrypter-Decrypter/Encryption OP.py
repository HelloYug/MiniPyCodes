#Yug's TXT DATA file Encrypter
#other info
width = 50

#heading
print ("-" * width)
print (("- Yug's Python Text Encrypter -").center (width))
print ("-" * width)

#password Protection
print ((" THE FILE IS PASSWORD PROTECTED ").center (width, "-"))
username = input("Enter your username: ")
pwd = input ("Enter your password: ")

count=0
while (username != "yugla") or (pwd != "1608"):
        print (("Either username or password mismatched").center (width, "-"))
        count += 1
        username = input("Enter your username: ")
        pwd = input ("Enter your password: ")
        
        if (username == "yugla") and (pwd == "1608"):
                continue
        
        if count == 1:
                print ((" Intruders not Allowed ").center(width, "-"))
                print ((" WARNING! "*3).center(width, "-"))
                print ((" Just Get Out! ").center(width, "-"))
                break
        
else:
        print ("\tlogging in...")
        print ("*"*width)
            
        #input
        string = input ("Enter Text: ")
        string = string.strip()
        print ("Text to be Encryped: ", string)
        
        #string formatting
        if (len(string)%2) == 1:
                string += "_"

        #inverted sentence
        invertedsentence = string[::-1]
                #print ("invertedsentence: ",invertedsentence)
        
        #Adding random character after every 2 characters
        from random import choice
        from string import yugmix
        listofyugmix = list (yugmix)
        updatedlistofyugmix = listofyugmix.remove ("_" and "^" and "$")
                #print (listofyugmix)

        randomizedsentence = ""
        for i in range(0, len(invertedsentence), 2):                 
                char = str (choice(listofyugmix))
                randomizedadding = invertedsentence[i:i + 2]+ char
                randomizedsentence += randomizedadding

                #print ("randomizedsentence: ", randomizedsentence)
        
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

        #Printing Output
        print ("\nEncrypted Text:", Encrypted_text)
        print ("-"*width)
