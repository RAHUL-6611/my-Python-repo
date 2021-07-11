from tkinter import *
from tkinter.ttk import *
from time import strftime

time = Tk()
time.title("My watch")
time.geometry("140x33")


def times():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, times)


label = Label(time, font="ds-digital 18 bold", background="black", foreground="cyan")
label.pack()
times()


time.mainloop()
