# This program converts the input kilograms into grams, pounds and ounces

from tkinter import *

window = Tk()


def kg_converter():
    grams = float(e1_value.get()) * 1000
    ounces = float(e1_value.get()) * 35.274
    pounds = float(e1_value.get()) * 2.20462

    t1.insert(END, grams)
    t2.insert(END, ounces)
    t3.insert(END, pounds)


b1 = Button(window, text="Convert", command=kg_converter)
b1.grid(row=0, column=2)

l1 = Label(window, text="KGs")
l1.grid(row=0, column=0)
e1_value = StringVar()

e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=15)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=15)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=15)
t3.grid(row=1, column=2)


window.mainloop()
