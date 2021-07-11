from tkinter import *
from PIL import ImageTk, Image


def every_100(text):
    final_text = ""

    for i in range(0, len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n\n"
    return final_text


gui = Tk()
gui.title("Parmaras-News")
gui.geometry("1000x800")
# --------------------------------------------------------------------------------

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i + 1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"img/{i + 1}.jpg")
    # Label(gui, text=image, bg="red")
    # TODO: resize is must
    image = image.resize((455, 455), Image.ANTIALIAS)   # retains the quality of image
    photos.append(ImageTk.PhotoImage(image))
# --------------------------------------------------------------------------------
f0 = Frame(gui, width=800, height=70)
Label(f0, text="Parmaras-News", font="lucida 33 bold").pack()
Label(f0, text="February 17 ,2021", font="lucida 13 bold").pack()
f0.pack()

f01 = Frame(gui, width=70, height=70)
Label(f01, text=texts[0], padx=2, pady=2, bg="gold", fg="brown", font="IMPACT 10 bold", relief=GROOVE, borderwidth=5)\
    .pack(side=RIGHT)
Label(f01, image=photos[0], anchor="e", bg="red", relief=GROOVE, borderwidth=5, padx=50).pack(side=LEFT)
f01.pack(anchor="w")


f02 = Frame(gui, width=450, height=70, padx=10)
Label(f02, text=texts[0], padx=12, pady=12, bg="gold", fg="brown", font="IMPACT 10 bold", relief=GROOVE, borderwidth=5)\
    .pack(side=RIGHT)
Label(f02, image=photos[0], anchor="e", bg="red", relief=GROOVE, borderwidth=5).pack(side=LEFT)
f02.pack(anchor="nw")


f03 = Frame(gui, width=450, height=70, padx=10)
Label(f03, text=texts[0], padx=12, pady=12, bg="gold", fg="brown", font="IMPACT 10 bold", relief=GROOVE, borderwidth=5)\
    .pack(side="left")
Label(f03, image=photos[0], anchor="e", bg="red", relief=GROOVE, borderwidth=5).pack(side=RIGHT)
f03.pack(anchor="nw")

gui.mainloop()
