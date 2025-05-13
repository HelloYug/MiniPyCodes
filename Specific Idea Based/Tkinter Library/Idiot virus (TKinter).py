# Importing module
from tkinter import messagebox, Button, Tk

root = Tk()
root.geometry("200x200")
def msg():
    for i in range (3):
        messagebox.showwarning("Alert","The user is an idiot!")

def msg2():
    for i in range (3):
        messagebox.showwarning("Alert","LOL, you are an idiot!")

but = Button (root, text = "Press if you are an idiot", command = msg)
but2 = Button (root, text = "Press if you are not!", command = msg2)

but.place(x=40,y=60)
but2.place (x= 48, y = 90)
root.mainloop()                 
