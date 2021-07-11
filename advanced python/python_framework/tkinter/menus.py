from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk, Image


def myfunc():
    print("Khatam ,Tata , Bye bye")


def helps():
    print("I will help you bro")
    a = tmsg.showinfo("Help", "Abhi Lunch time hai !")
    print(a)


def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this GUi... Was your experience good?")
    if value == "yes":
        msgi = "Great. Rate us on appstore please"
    else:
        msgi = "oh! we are sorry, tell us what went wrong. we will call you soon"
    tmsg.showinfo("Experience", msgi)
    print(value)


def exits():
    a = tmsg.showwarning("Warning", "Do you really want to quit")
    print(a)


def full():
    v = tmsg.askyesno("Fullscreenmode", " Do you want Fullscreen?")
    print(v)
    if v:
        menus.attributes('-fullscreen', True)
    elif not v:
        menus.geometry(f"{a}x{b}")


def retrybro():
    a = tmsg.askretrycancel("ERROR", " Kindly try again")
    print(a)

    if a:
        msgs = "python is not installed"
    elif not a:
        msgs = "Command request cancelled"
    tmsg.showinfo("Details", msgs)


user = int(input("How big window you want : 1.small 2.medium 3.large 4. XXL"))

if user == 1:
    a = 200
    b = 200
elif user == 2:
    a = 400
    b = 400
elif user == 3:
    a = 600
    b = 600
else:
    a = 1355
    b = 710


def switch():
    myslider.config(bg="red")
    myslider.set(50)
    print(f" Battery remaining {myslider.get()} %")
    tmsg.showinfo("DETAILS", "Congrats, battery saved by 66%")
    # myslider = Scale(menus, from_=100, to_=100, orient=HORIZONTAL)


menus = Tk()
menus.title("PTU-student")
menus.geometry(f"{a}x{b}")

abc = Frame(menus, width=200, height=350)
Label(abc, text=" Data saver mode:  ").pack()
myslider = Scale(abc, from_=0, to=100, orient=HORIZONTAL, tickinterval=50, bg="black", fg="grey")
myslider.pack(pady=1)
Button(abc, text="ON/OFF", command=switch).pack(pady=10)
abc.pack(anchor="ne", side=RIGHT)
# ------------------------------------------------------------------
mymenu = Menu(menus)  # i want menu named mymenu inside menus

# ------------------------------------------------------------------
m1 = Menu(mymenu, tearoff=0)
m1.config(bg="grey")
mymenu.add_cascade(label="File", menu=m1)

m2 = Menu(mymenu, tearoff=0)
m2.config(bg="grey", fg="black")
mymenu.add_cascade(label="Tools", menu=m2)
m2.add_command(label="full-screen", command=full)

m1.add_command(label="New project", command=myfunc)
m1.add_command(label="New ", command=myfunc)
m1.add_command(label="New Scratch File", command=myfunc)
m1.add_separator()

m3 = Menu(mymenu, tearoff=0)
m1.add_cascade(label="Open", menu=m3, command=myfunc)
m3.add_command(label="Python file", command=retrybro)

m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Open recent", command=myfunc)
m1.add_command(label="Close project", command=myfunc)
m1.add_command(label="Rename project..", command=myfunc)
m1.add_separator()
m1.add_command(label="Settings", command=myfunc)
m1.add_command(label="File properties", command=myfunc)
m1.add_separator()
m1.add_command(label="Local History", command=myfunc)
m1.add_separator()
m1.add_command(label="Save all", command=myfunc)
m1.add_command(label="", command=myfunc)
m1.add_command(label="Rename project..", command=myfunc)
m1.add_command(label="Reload all from Disk\n Invalidate Caches/ Restart..", command=myfunc)
m1.add_separator()
m1.add_command(label="Manage IDE settings", command=myfunc)
m1.add_command(label="New project settings", command=myfunc)
m1.add_separator()
m1.add_command(label="Export", command=myfunc)
m1.add_command(label="Print", command=myfunc)
m1.add_command(label="Add to Favourites", command=myfunc)
m1.add_separator()
m1.add_command(label="Power Save Mode", command=myfunc)
m1.add_separator()
m1.add_command(label="Exit", command=exit)

mymenu.add_command(label="Edit", command=myfunc)
mymenu.add_command(label="View", command=myfunc)
mymenu.add_command(label="Navigate", command=myfunc)
mymenu.add_command(label="Code", command=myfunc)
mymenu.add_command(label="Refactor", command=myfunc)
mymenu.add_command(label="Run", command=myfunc)

mymenu.add_command(label="VCS", command=rate)
mymenu.add_command(label="Window", command=myfunc)
mymenu.add_command(label="Help", command=helps)
mymenu.add_command(label="Exit", command=exits)
menus.config(menu=mymenu, bg="grey")

abcd = Frame(menus, pady=30)
abcd.config(bg="darkgrey")
Label(abcd, text="PTU...forstudents", font="IMPACT 40 italic",
      bg="black", fg="silver", padx=20, borderwidth=1, relief=GROOVE).pack(fill=X)
abcd.pack(anchor="n", fill=X)

# image = Image.open("appimg.png")
# image = image.resize((1245, 400), Image.ANTIALIAS)
# photos.append(ImageTk.PhotoImage(image))

photo1_file = Image.open("Pondicherry-Engineering-Col.jpg")
photo1_file = photo1_file.resize((1245, 400), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(photo1_file)
photo_label1 = Label(image=photo1)
photo_label1.pack()

# photo2 = Image.open("appimg.png")
# photo2 = photo2.resize((1245, 400), Image.ANTIALIAS)
# photo2 = ImageTk.PhotoImage(photo2)
# photo_label2 = Label(image=photo2)                 # to use jpg image you  need to use imageTk
# photo_label2.pack()

p = Canvas(menus, width=a, height=b)
p.pack()
# p.create_rectangle(a+20, b, a+20, b)
p.create_rectangle(0, 0, 1245, 800, fill='red')
# p.create_polygon(5, 36, 700, 700, fill='red')
menus.mainloop()
