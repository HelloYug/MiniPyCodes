# Personality Checker
# Importing module
from random import choice

# Other Information
width = 42

# Listing Personality Traits
per = [
    "Smart", "Cool Dude", "Dashing", "Intelligent", "Sundar-Shushil log", "Faithful", "Trustworthy",
    "Honest", "Brave", "Loyal", "Confident", "Hard-Working", "Courageous", "Selfish", "Selfless",
    "Neat & clean", "Popular", "Messy", "Gentle", "Joyful", "Mischievous", "Patriotic", "Pretty",
    "Achiever", "To be successful", "Leader", "Simple", "Creative", "Fancy", "Daring", "Humorous",
    "Lazy", "Active", "Energetic", "Lovable", "Ambitious", "Curious", "Clever", "Cunning",
    "Helpful", "Cooperative", "Bossy", "Pitiful", "Cheerful", "Pleasing", "Introvert", "Extrovert",
    "Always Happy", "Dukhi Aatma", "Shy", "Adventurous", "Keen", "Thoughtful", "Demanding", "Witty",
    "Arrogant"
]

length = len(per)
print("No. of Personality traits available:", length)
love = 10

# Heading
while True:
    print("-" * width)
    print("*" * width)
    print(("Personality checker").center(width))
    print("*" * width)
    
    # Input
    name = input("Enter your name or DOB: ")
    while name == "" or isinstance(name, int):
        print("Enter Valid name!")
        name = input("\nEnter your name or DOB: ")
        if isinstance(name, str):
            break
        
    print(("Max: 10").rjust(width))
    no = int(input("Enter the number of traits you want to know: "))

    while no <= 0 or no > love:
        print(f"\nEnter a valid number! \nEnter a number between 1 and {love}")
        no = int(input("Enter the number of traits you want to know: "))
    
    # Output printing
    print("\nPersonality Trait(s): ", end="")
    for x in range(no):
        if x < no - 1:
            print(choice(per), end=", ")
        if x == no - 1:
            print(choice(per), end=".")

    print()
    print("-" * width)
    ca = input("Do you want to know someone else's personality traits? (yes/no): ")
    if ca.lower() in ["n", "no"]:
        print("OK")
        break
    else:
        continue
