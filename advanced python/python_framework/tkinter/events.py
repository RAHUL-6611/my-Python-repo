from tkinter import *


def prevent(event):
    print(f"clicked at {event.x}, {event.y}")


events = Tk()


w = 600
h = 400
events.geometry(f"{w}x{h}")

widget = Button(events, text='hello')
widget.pack()     # always write separately
widget.bind("<Button-1>", prevent)
widget.bind("<Double-1>", quit)


events.mainloop()