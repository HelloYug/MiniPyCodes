# Importing required modules
from tkinter import messagebox, Button, Tk

# Setting up the Tkinter window
root = Tk()
root.geometry("200x200")

# Function for showing the first message
def msg():
    for i in range(3):
        messagebox.showwarning("Alert", "The user is an idiot!")

# Function for showing the second message
def msg2():
    for i in range(3):
        messagebox.showwarning("Alert", "LOL, you are an idiot!")

# Creating buttons and placing them on the window
but = Button(root, text="Press if you are an idiot", command=msg)
but2 = Button(root, text="Press if you are not!", command=msg2)

# Placing buttons at specific positions
but.place(x=40, y=60)
but2.place(x=48, y=90)

# Running the main event loop
root.mainloop()
