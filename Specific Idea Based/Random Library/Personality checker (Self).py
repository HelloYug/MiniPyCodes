#importing module
from random import choice

#other info
width=42

#listing Personality Traits
per = ["Smart", "Cool Dude", "Dashing", "Intelligent",
      "Sundar-Shushil log", "faithful", "Trustworthy",
      "Honest", "Brave", "Loyal", "Confident",
      "Hard-Working", "Courageous", "Selfish", "Selfless",
      "Neat & clean", "Popular", "Messy", "Gentle",
      "Joyful", "Mischievous", "Patriotic", "Pretty",
      "Achiever", "To be successful", "Leader", "Simple",
      "Creative", "Fancy", "Daring", "Humourous",
      "Lazy", "Active", "Energetic", "Lovable",
      "Ambitious", "Curious", "Clever", "Cunning",
      "Helpful", "Cooperative", "Bossy", "Pitful",
      "Cheerful", "Pleasing", "Introvert", "Extrovert",
      "Always Happy", "Dukhi Aatma", "Shy", "Adventurous",
      "Keen", "Thoughtful", "Demanding", "Witty"
      "Arrogant"]

length= len(per)
print ("No. of Personality traits available:", length)
#love=int (length/5)
love= 10

#heading
while True:
    print ("_"*width)
    print ("*"*width)
    print (("Personality checker").center (width))
    print ("*"*width)
    
    #input
    name= input ("Enter your name or DOB: ")
    while name=="" or name==int:
        print ("Enter Valid name!")
        name= input ("\nEnter your name or DOB: ")
        if name==str:
            break
        
    #print ("\t\t\tMin= 1 & Max=", love)
    print (("Max: 10").rjust(width))
    no= int (input ("Enter no. of traits you want to know: "))

    '''
    while no<=0 or no>love:
        print ("\nEnter Valid no.! \nEnter a no. between 1 and", love)
        no= int (input ("Enter no. of traits you want to know: "))
        print ()
        if no>0 and no<love:
            break
    '''
    while no<=0 or no>love:
            print ("\nEnter Valid no.! \nEnter a no. between 1 and", love)
            no= int (input ("Enter no. of traits you want to know: "))
            print ()
            if no>0 and no<love:
                break
    
    #output printing
    print ("\nPersonality Trait(s): ",end="")
    for x in range (no+1):
        if x<no-1:
            print (choice(per),end= ", ")
        if x==no:
            print (choice(per),end= ".")

    print ()
    print ("-"*width)
    Ca= input ("Do you want to know someone else's personality traits?")
    if Ca=="n":
        print ("OK")
        break
    else:
        continue
