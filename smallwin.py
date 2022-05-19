#!/usr/bin/env python3
try:
    # for Python2
    from tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

Root=Tk()
Root.geometry('450x450')

Root.config(background = "white")

Btn1=Button(Root, text="Where is the Green background ?", background='green', foreground='blue').pack()
Btn2 = Button(Root, text = 'No red background', bg='red', fg='blue').pack()

mainloop()