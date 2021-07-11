from tkinter import *

button = Tk()

button.title = "ClickBait"
button.geometry("644x333")


def hello():
    print("Hello, i hacked you")


frame = Frame(button, borderwidth=1, bg="grey", relief=GROOVE, pady=15)
frame.pack(side=LEFT, anchor="n")

b1 = Button(frame, text="Click Now", fg="white", bg="Black", font=55, command=hello)  # only name, not hello()
b1.pack(side=LEFT, anchor="n")


b2 = Button(frame, text="Click Now", fg="white", bg="Black", font=55)
b2.pack()
button.mainloop()
