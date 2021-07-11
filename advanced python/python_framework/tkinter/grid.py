from tkinter import *

grids = Tk()

grids.title("LAYOUT")
grids.geometry("655x333")
# -------------------------------------------


def setval():
    print(f" Username: {uservalue.get()}")
    print(f" Password: {passvalue.get()}")


user = Label(grids, text="Username")
password = Label(grids, text="Password")
user.grid(row=0)       # on row 1
password.grid(row=1)   # on row 2

# Variable Classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()      # will take string as input
passvalue = StringVar()

userentry = Entry(grids, textvariable=uservalue)
passentry = Entry(grids, textvariable=passvalue)

userentry.grid(row=0, column=1)  # on column 2 and row 1
passentry.grid(row=1, column=1)  # on colmn 2 and row 2

Button(text="Submit", command=setval).grid()
grids.mainloop()
