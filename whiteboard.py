# Name: Jerico James F. Viteño
# Laboratory Exercise 3: Whiteboard
# November 19, 2022

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="f2f3f5")
root.resizable(False,False)

#icon
pencil = PhotoImage(file="pencil.png")
root.iconphoto(False,pencil)

holder = PhotoImage(file="holder.png")
Label(root,image=holder,bg="f2f3f5").place(x=10,y=20)


root.mainloop()