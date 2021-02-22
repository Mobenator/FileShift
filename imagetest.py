#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter

 

window = tkinter.Tk()
window.title('My Window')
window.geometry('100x100')
 
l = tkinter.Label(window, bg='white', width=20, text='empty')
l.pack()
 
def print_selection():
    if (imgCheckVal.get() == 1) & (vidCheckVal.get() == 0):
        l.config(text='Images')
    elif (imgCheckVal.get() == 0) & (vidCheckVal.get() == 1):
        l.config(text='Videos')
    elif (imgCheckVal.get() == 0) & (vidCheckVal.get() == 0):
        l.config(text='Nothing')
    else:
        l.config(text='Images and videos')
 
imgCheckVal = tkinter.IntVar()
vidCheckVal = tkinter.IntVar()
imgCheckBox = tkinter.Checkbutton(window, text='Images',variable=imgCheckVal, onvalue=1, offvalue=0, command=print_selection)
imgCheckBox.pack()
vidCheckBox = tkinter.Checkbutton(window, text='Videos',variable=vidCheckVal, onvalue=1, offvalue=0, command=print_selection)
vidCheckBox.pack()



window.mainloop()