from Tkinter import *
import tkMessageBox
import Tkinter as tk

top = tk.Tk()
top.configure(background='#8A4B35')

top.configure(background='#8A4B35')
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

top.geometry("800x400")

space = 32
maxcoord = 4

buttons = {}
rows = []
for z in range(-maxcoord, maxcoord+1):
    row = []
    for y in range(maxcoord, -maxcoord -1 , -1):
        x = 0 - z - y
        if x in range(- maxcoord, maxcoord + 1):
            row.append((x, y, z))
            buttons[(x, y, z)] = tk.Button(top, command=helloCallBack)
            buttons[(x, y, z)].pack()
    rows.append(row)

for row in rows:
    result = ""
    makeup = maxcoord * 2 + 1 - len(row)
    for i in range(len(row)):
        indent = (maxcoord * 2 + 1 - len(row))
        x,y,z = row[i]
        buttons[row[i]].place(bordermode=OUTSIDE, height=space, width=space,
                                 x= space * 6 + makeup * (space + 2)/2 + (space + 2) * i,
                              y= space * 6 + (space + 2) * z)

top.mainloop()