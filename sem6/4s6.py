from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        colour_first =format.get()
        AA=hex(255-int(colour_first[:2],16))[2:]
        BB=hex(255-int(colour_first[2:4],16))[2:]
        CC=hex(255-int(colour_first[4:6],16))[2:]
        colour=AA+BB+CC
        ttk.Label(mainframe, text=colour_first, background=('#'+colour_first)).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe,text=colour, background=('#'+colour)).grid(column=2, row=2, sticky=(W, E))
    except ValueError:
        pass


root = Tk()
root.title("Colour compatibility")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

format = StringVar()
format_entry = ttk.Entry(mainframe, width=10, textvariable=format)
format_entry.grid(column=2, row=1, sticky=(W, E))


ttk.Button(mainframe, text="Show", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Colour").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Complementary colour").grid(column=3, row=2, sticky=W)
color0=format.get()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

format_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()