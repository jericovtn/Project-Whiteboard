# Name: Jerico James F. Viteño
# Laboratory Exercise 3: Whiteboard
# November 19, 2022

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("White Board")
root.geometry("1050x570+130+50")
root.resizable(False,False)

canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1')
canvas.bind('B1-Motion')


root.mainloop()