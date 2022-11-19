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

currentX = 0
currentY = 0
color = 'black'

def locateXY(work):
    global currentX, currentY 
    currentX = work.x
    currentY = work.y

def addLine(work):
    global currentX, currentY 
    canvas.create_line((currentX, currentY, work.x, work.y), 
    width=getCurrentValue(), fill=color, capstyle=ROUND, smooth=TRUE)
    currentX, currentY = work.x, work.y

def showColor(new_color):
    global color
    color = new_color

def newCanvas():
    canvas.delete('all')
    displayPalette()

button = Button(root, text = 'Clear', bd='5', command=newCanvas).place(x=30, y=400)

#Colors
colors = Canvas(root, bg='#ffffff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

def displayPalette():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('black'))

    id = colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('gray'))
   
    id = colors.create_rectangle((10,70,30,90),fill='brown4')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('brown4'))
   
    id = colors.create_rectangle((10,100,30,120),fill='red')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('red'))
    
    id = colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('orange'))
   
    id = colors.create_rectangle((10,160,30,180),fill='yellow')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('yellow'))
    
    id = colors.create_rectangle((10,190,30,210),fill='green')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('green'))
    
    id = colors.create_rectangle((10,220,30,240),fill='blue')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('blue'))
    
    id = colors.create_rectangle((10,250,30,270),fill='purple')
    colors.tag_bind(id, '<Button-1>',lambda x: showColor('purple'))

    
displayPalette()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>', locateXY)
canvas.bind('<B1-Motion>', addLine)

currentValue = tk.DoubleVar()

def getCurrentValue():
    return '{: .2f}'.format(currentValue.get())

def slider_changed(event):
    valueLabel.configure(text=getCurrentValue())

# Slider
slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, 
variable=currentValue)
slider.place(x=30, y=530)

# Value Label
valueLabel = ttk.Label(root,text=getCurrentValue())
valueLabel.place(x=27, y=550)

root.mainloop()