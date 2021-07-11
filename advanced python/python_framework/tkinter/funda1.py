# other than tkinter, what are the other GUi tools ?  - wxpython

from tkinter import *

# from PIL import Image, ImageTk

rahul = Tk()

# title
rahul.title("Parmaras")

# width X height:
rahul.geometry("844x634")
rahul.minsize(200, 100)  # (width,height)
rahul.maxsize(1350, 988)


# important Label options :
# text - add text
# bd -background
# fg -foreground
# font = sets the font  /font=" comicsansms 19 bold " //or// font=("comicsansms", 19, "bold")
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN ,RAISED,GROOVE, RIDGE
# ---------------------------------------------------------------
# important Pack options
# anchor = "nw","ne","se","sw",
# side = TOP, BOTTOM ,LEFt ,RIGHT
# fill
# padx
# pady


def home():
    print("THIS IS : Home")


def about():
    print("THIS IS: About")


def menu():
    print("THIS IS: Menu")


def page1():
    print("THIS IS: Page1")


def page2():
    print("THIS IS: Page2")


def page3():
    print("THIS IS: Page3")


def head():
    print("THIS IS: Head")


# Label:
sarayu = Label(text=" Parmaras Editing Tool ")
sarayu.pack()

paragraph = Label(text='''Rahul parmar is a software engineer.\n
 indeed he is working hard to make things work\n''', bg="red", fg="White", padx=23, pady=24, font=("comicsansms", 9,
                                                                                                   "bold"),
                  borderwidth=3, relief=GROOVE)
paragraph.pack(anchor="se", side=BOTTOM, fill=X)  # but anchor cannot move it, use (side)

# Frames - divisions
frame2 = Frame(rahul, bg="green", borderwidth=3, relief=GROOVE)
frame1 = Frame(rahul, bg="orange", borderwidth=3, relief=GROOVE)
frame3 = Frame(rahul, bg="yellow", borderwidth=3, relief=GROOVE)

frame2.pack(side=TOP, anchor="ne", fill=X)
frame1.pack(side=LEFT, anchor="nw", fill=Y)
frame3.pack(side=RIGHT, anchor="ne", fill=Y)

Button_for_frame101 = Button(frame1, text="HOME\n", bg="Orange", font=30, fg="Black",
                             padx=10,
                             pady=10, command=home)
Button_for_frame101.pack(fill=X)

Button_for_frame102 = Button(frame1, text="ABOUT\n", bg="Orange", font=30, fg="Black", padx=10,
                             pady=10, command=about)
Button_for_frame102.pack(fill=X)

Button_for_frame103 = Button(frame1, text="MENU\n", bg="Orange", font=30, fg="Black",
                             padx=10,
                             pady=10, command=menu)
Button_for_frame103.pack(fill=X)

Button_for_frame2 = Button(frame2, text="Parmaras Technology", font=30, bg="Black", fg="White", padx=10,
                           pady=10, command=head)
Button_for_frame2.pack(fill=X)

Button_for_frame301 = Button(frame3, text="Page 1", bg="Yellow", font=30, fg="Black",
                            padx=10, pady=10, command=page1)
Button_for_frame301.pack(fill=Y)

Button_for_frame302 = Button(frame3, text="Page 2", bg="Yellow", font=30, fg="Black",
                            padx=10,
                            pady=10, command=page2)
Button_for_frame302.pack(fill=Y)

Button_for_frame303 = Button(frame3, text="Page 3", bg="Yellow", font=30, fg="Black",
                            padx=10,
                            pady=10, command=page3)
Button_for_frame303.pack(fill=Y)

# image:
# photo = PhotoImage(file="appimg.png")
# photo_label = Label(image=photo)
# photo_label.pack()

# photo2 = ImageTk.PhotoImage(file="filename.jpg")
# photolabel2 = Label(image=photo2)                 # to use jpg image you  need to use imageTk
# photolabel2.pack()

# gui logic here
rahul.mainloop()  # event loop
