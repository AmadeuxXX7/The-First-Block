import tkinter as tk
from tkinter import *

root = Tk()

root.title("Block Code")

root.resizable(True, True)
root.geometry("800x500")
icon = tk.PhotoImage(file="imgs/logo.png")
root.iconphoto(True, icon)

block = Frame(root)
block.grid(row=1, column=1, padx=20, pady=(20, 0), sticky='nsew')

# Configure grid weights to allow resizing
block.grid_rowconfigure(0, weight=1)
block.grid_rowconfigure(1, weight=1)
block.grid_rowconfigure(2, weight=1)
block.grid_rowconfigure(3, weight=1)
block.grid_columnconfigure(1, weight=1)

block_main_body = Frame(block, bg="yellow")
block_main_body.grid(row=1, column=1, sticky='ew')

text = Label(block_main_body, text="This is a test block", bg="yellow")
text.grid(row=1, column=1, pady=5, sticky='w')

def setEntry(event):
    new_width = max(3, len(entry.get()))
    entry.config(width=new_width)

entry = tk.Entry(block_main_body, width=3)
entry.grid(row=1, column=2, padx=5, sticky='w')

entry.bind("<KeyRelease>", setEntry)

underblock = Frame(block, bg="yellow", height=5)
underblock.grid(row=2, column=1, sticky='ew')

tab = Frame(block, bg="yellow", width=22, height=10)
tab.grid(row=3, column=1, sticky='w', padx=22) 

blank1 = Frame(block, bg="yellow", width=22, height=10)
blank1.grid(row=0, column=1, sticky='w')

blank2 = Frame(block, bg="yellow", height=10)
blank2.grid(row=0, column=1, sticky='ew', padx=(44, 0))

root.mainloop()