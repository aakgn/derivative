#@author: ali akgün
#@date: 30.12.2020
#@brief: Gui application of forward_differention.py
#@to do: help section !!!
#about section
#graph of input and output function.
#change variable names !!!
#@brief:
#

from tkinter import *

app = Tk()

app.title("forward differention")
app.geometry("")

part_text = StringVar()
part_label = Label(app, text = "Function:", font = ("bold", 14), pady = 20)
part_label.grid(row = 0, column = 0, sticky = W)
part_entry = Entry(app, textvariable = part_text)
part_entry.grid(row = 0, column = 1)
