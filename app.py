import tkinter as tk
from tkinter import Text, filedialog
import os

root =  tk.Tk()

root.title("Adasiak'a App")
canvas = tk.Canvas(root, height=600, width=800, bg= "#263D42" )

canvas.pack()

frame = tk.Frame(root,  bg= "white" )
frame.place(relwidth=0.8 , relheight=0.8)

root.mainloop()