# In this lecture we are going to cover the usage of Tkinter, a library
# which allows to create Graphical User Interfaces (GUI) in Python
# Tkinter doesn't need any installation since it is integrated in python

# We import each tkinter module because we are going to use a lot of Tkinter
# elements, and this way we don't need to address them using always the
# tkinter.something prefix

from tkinter import *

# A tkinter program is made of:
# - Window
# - Widgets

# First of all the window has to be created

window = Tk()

# Everything inside the window goes here

# We'll use the following function later
# That's a callback fucntion we want to activate pressing the button
# we put inside the window.

# e1_value is a StringVar() object (defined later).
# To get the default python string, it is needed the get() method.


def km_to_miles():

    # We want to insert a value in the text widget we create later
    # Parameters:
    # - END: Put the passed text at the end of the widget
    # - miles: The value we want to print

    # We convert the input km in miles

    miles = float(e1_value.get()) * 1.6

    t1.insert(END, miles)

# Let's create a button widget
# To see which are the parameters the function takes, type "Button?"
# into a Python interactive shell.

# In our case, we used:
# - window: The window the button has to be displayed in
# - text = "Execute": The text embedded in the button


b1 = Button(window, text="Execute", command=km_to_miles)

# We need to tell Tkinter where we want the button to be placed:

# b1.pack()

# There is another way to put widgets in the window
# Decomment it to try, and delete the previous b1.pack() line

b1.grid(row=0, column=0)

# We create a StringVar object, that's needed by the Entry constructor
# in order to store what you write inside the Entry in a variable.
e1_value = StringVar()

# We want to create some entries (Area where we can enter values)

e1 = Entry(window, textvariable=e1_value)

# We place it next to the button

e1.grid(row=0, column=1)

# Text widget:

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# We now want to connect the graphical items to some code behavior
# E.G.: We want to input a certain amount in miles and get
#       the corresponding value in kilometers, when we press "Execute"

# To do this, we need to link a function to the button we created.
# That's done by putting a "command" parameter in the button definition
# (You will find it already inserted, at line 51)
# b1 = Button (..., command = km_to_miles)
# That means that when the button is pressed, the function "km_to_miles"
# gets triggered.


window.mainloop()
