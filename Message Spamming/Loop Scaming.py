WebsiteOpeningTime = float (input ("Enter website wait time: "))
print ()
Reciever = input ("Enter the Chat or Group name you want to spam: ")
message = input ("Enter the message you want to spam: ")
SpamTime = int (input ("Enter the no. of times you want to spam the message :"))
print ()



import FGDM
FGDM.OpenBrowser("web.whatsapp.com", WebsiteOpeningTime)
FGDM.Group (Reciever)
FGDM.writing (message)
