# you can either use pack or grid don't use both
from tkinter import *

canvass = Tk()
w = 600
h = 400
canvass.geometry(f"{w}x{h}")
canvass.title("Canvas stuff")
a = Canvas(canvass, width=w, height=h)
a.pack()
a.create_line(0, 0, 800, 400, fill="red")
a.create_rectangle(10, 10, 50, 50)
a.create_text(400, 200, text="python", font="serif 90 bold")
# create_line
# create_rectangle
# create_oval
# create_text
# and search many more

canvass.mainloop()