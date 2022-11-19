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
root.configure(bg='#f2f3f5')
root.resizable(False,False)

# icons


current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x, current_y 
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y 
    canvas.create_line((current_x, current_y, work.x, work.y), width=2, fill=color)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    displayPalette()

#Colors
colors = Canvas(root, bg='#ffffff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

def displayPalette():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('gray'))
   
    id = colors.create_rectangle((10,70,30,90),fill='brown4')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('brown4'))
   
    id = colors.create_rectangle((10,100,30,120),fill='red')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('red'))
    
    id = colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('orange'))
   
    id = colors.create_rectangle((10,160,30,180),fill='yellow')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('yellow'))
    
    id = colors.create_rectangle((10,190,30,210),fill='green')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('green'))
    
    id = colors.create_rectangle((10,220,30,240),fill='blue')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('blue'))
    
    id = colors.create_rectangle((10,250,30,270),fill='purple')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('purple'))

    
displayPalette()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)




root.mainloop()