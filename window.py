
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
 
# creates a PythonWindow() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("400x400")
# master.color("white")
 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("300x300")
    
    newWindow.background("white")
    newWindow.color("white")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
    # Kolor.color(white)
 
 
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()