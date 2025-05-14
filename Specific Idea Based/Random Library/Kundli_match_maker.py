# Importing modules
import random
from HandyPy.formatters import AniType  # refer to https://github.com/HelloYug/MiniPyCodes/blob/main/HandyPy/formatters.py

# Other Information
width = 35

# Heading
print("-" * width)
print(("Kundli Match Maker").center(width))
print("-" * width)

# Inputs
n1 = input("Enter Your Name \t : ")
n2 = input("Enter Your Partner's name: ")
print()

# Processing
res = random.randint(8, 36)

# Printing output
print(f"Aapke {res} Gun milte hain!")
hehe = "-" * (int((res - 5) / 4))

print("[", end="")
AniType(hehe, 0.03, 0.2)  # Animating the first part
print(f" {res} ", end="")
AniType(hehe, 0.03, 0.2)  # Animating the second part
print("]")

print(n1, "❤", n2)
