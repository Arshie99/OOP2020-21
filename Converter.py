# This is an example to illustrate how to use
# TKinter and TTK
# The example is adapted from https://tkdocs.com/tutorial/firstexample.html
# accessed Oct 2020
# author: B. Schoen-Phelan
# OOP Python Semester 1
# week 5: GUI with Python

from tkinter import * # imports all tkinter libraries
from tkinter import ttk # overwrites tkinter widget libraries with ttk widgets instead
                        # the order of import is therefore important!

class Converter:
    def __init__(self):
        self.init_window() # it's good practice to separate logical functionality

    # this function creates the GUI
    def init_window(self):
        root = Tk() # the window
        root.title("Feet to Meters") # title for the window

        mainframe = ttk.Frame(root, padding="3 3 12 12") # main content frame inside the window
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # align to all sides
        root.columnconfigure(0, weight=1) # padding on resizing
        root.rowconfigure(0, weight=1) # padding on resizing

        self.feet = StringVar() # Text box, self allows access from outside this function
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet) # set fixed size
        feet_entry.grid(column=2, row=1, sticky=(W, E)) # add to main frame with fixed position

        self.meters = StringVar() # Text box, self allows access from outside this function
        ttk.Label(mainframe, textvariable=self.meters)\
            .grid(column=2, row=2, sticky=(W, E)) # backslash allows break of
                                                  # very long lines of code

        ttk.Button(mainframe, text="Calculate", command=self.calculate_conversion)\
            .grid(column=3, row=3, sticky=W)

        # 3 static labels to explain to the user what to do here
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # go through all widgets and adds a bit of padding to make
        # the interface look less squashed,
        # could have been done manually above
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # focus with the cursor goes to the text field
        feet_entry.focus()

        # pressing return has the same effect as
        root.bind("<Return>", self.calculate_conversion)

        # makes everything appear on screen
        root.mainloop()


    # helper function to calculate the conversion from feet to meters
    # takes no arguments
    # returns no arguments
    # sets values directly
    # not great OOP here, but works; we will learn how to do it
    # the real OOP way in a few weeks
    def calculate_conversion(self):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError as ve:
            self.meters.set(ve)


# creates an instance of Converter,
# because of this line the program starts with
# jumping into __init__
c = Converter()