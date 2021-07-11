from tkinter import *

rahuly = Tk()

rahuly.title("Ready")

rahuly.geometry("500x250")
rahuly.minsize(200, 100)
rahuly.maxsize(1000, 600)

footer = Label(text="READY", bg="lightpink", font="comicsansms 25 bold", borderwidth=30, padx=50, pady=20, relief=GROOVE
, fg="blue")
footer.pack(side=BOTTOM, fill=X, anchor="se")


rahuly.mainloop()