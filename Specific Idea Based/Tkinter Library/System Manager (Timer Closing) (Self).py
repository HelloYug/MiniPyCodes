# Importing necessary modules
from datetime import datetime, timedelta
from time import sleep
from tkinter import Button, Label, Tk
from pyautogui import hotkey, press, moveRel

# Other info
width = 50
FONT = "Calibri"

# Heading
print('*' * width)
print('Python System Manager'.center(width))
print('*' * width)

# Choices
print("Select an option:")
print("\t1. Shut Down")
print("\t2. Sleep Mode")
print("\t3. Exit")

# Inputs
choice = int(input("Enter your choice: "))

print('*' * width)  # Finishing line

# main program (Choice management)
flag = 0
if choice == 1:
    plan = "Shutting down system in..."
    plan1 = "System Shutdown"
elif choice == 2:
    flag = 1
    plan = "Putting system on sleep in..."
    plan1 = "System on Sleep"
elif choice == 3:
    print("OK!")
    from sys import exit
    exit()

# main program (working)
timer = float(input("Enter timer in minutes: "))
timer = int(timer * 60)

print("Current Time:", datetime.now().strftime("%H:%M:%S %d-%m-%Y (%a)"))
print("Command Time:", (datetime.now() + timedelta(seconds=timer)).strftime("%H:%M:%S %d-%m-%Y (%a)"))

# Simulating mouse movement to prevent sleep mode
while timer > 15:
    sleep(1)
    timer -= 1
    if timer % 10 == 0:
        moveRel(0, 2, 0.5)

# Tkinter window setup
root = Tk()
root.geometry("400x125")
root.config(bg="black")
root.title(plan)
root.attributes('-topmost', True)

# Countdown function
def TT(timer):
    while timer >= 0:
        alpha.config(text=f"{timer} Seconds")
        root.update()
        sleep(1)
        timer -= 1

    alpha.config(text=plan1, font=(FONT, 26))
    root.update()
    root.quit()
    sleep(1)
    root.destroy()

# Cancel button function
def cancel():
    sleep(0.2)
    root.destroy()
    print("Cancelled")
    from sys import exit
    exit()

# UI components
alpha = Label(root, background="black", foreground="white", font=(FONT, 40, "bold"))
but = Button(root, text="Cancel", command=cancel)
but.place(x=320, y=85)
alpha.pack()

# Start the countdown
TT(timer)
root.mainloop()

# Trigger system actions
sleep(1)
hotkey("win", "D")
hotkey("win", "M")
sleep(2)
hotkey("alt", "f4")
if flag == 1:
    press("up")
press("enter")
