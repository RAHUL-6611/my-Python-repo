from tkinter import *

travel = Tk()

# def back(event):
#     print("okay,heading back")
#     print(f"You clicked on the button at {event.x}, {event.y}")


travel.geometry("644x333")
travel.title("Travelform")


def prints(event):
    print(f"You clicked on this at {event.x}, {event.y}")
    print(
        f"{namevalue.get(), numvalue.get(), gendervalue.get(), contactvalue.get(), paymentvalue.get(), foodservice.get()}"
        f"\n")

    with open("data.txt", "a") as d:
        d.write(f"{namevalue.get(), numvalue.get(), gendervalue.get(), contactvalue.get(), paymentvalue.get(), foodservice.get()}\n")


# widget = Button(travel, text="Back").pack()
# widget.bind('<Button-1>', back)
# widget.bind("Double-1>", quit)


a = Label(travel, text="Welcome to parmar travel", font="comicsansms 19 bold", fg="blue",
          bg="green", anchor="n").grid(row=0, column=3)

name = Label(travel, text="Name: ").grid(row=6, column=2)
num = Label(travel, text="Phone: ").grid(row=7, column=2)
gender = Label(travel, text="Gender: ").grid(row=8, column=2)
contact = Label(travel, text="Contact: ").grid(row=9, column=2)
payment = Label(travel, text="Payment Mode: ").grid(row=10, column=2)

namevalue = StringVar()
numvalue = IntVar()
gendervalue = StringVar()
contactvalue = StringVar()
paymentvalue = StringVar()
foodservice = IntVar()

nameEntry = Entry(textvariable=namevalue).grid(row=6, column=3)
numEntry = Entry(textvariable=numvalue).grid(row=7, column=3)
genderEntry = Entry(textvariable=gendervalue).grid(row=8, column=3)
contactEntry = Entry(textvariable=contactvalue).grid(row=9, column=3)
paymentEntry = Entry(textvariable=paymentvalue).grid(row=10, column=3)

checkbox = Checkbutton(text="Are you a girl, get 10% off on tickets, Use #iamgirl", variable=foodservice).grid(row=11,
                                                                                                               column=3)
submit = Button(travel, text="Submit", bg="Black", fg="Yellow")
submit.grid(row=12, column=3)

submit.bind('<Button-1>', prints)
submit.bind('<Double-1>', quit)
travel.mainloop()
