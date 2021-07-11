from os import terminal_size
from playsound import playsound

text = input("please comment : ")
spam = 0

if("cash" in text):
    spam = 1
    playsound("scam_1992_intro_tune.mp3")

elif("make money online" in text):
    spam = 1
    playsound("scam_1992_intro_tune.mp3")

elif("buy now" in text):
    spam = 1
    playsound("scam_1992_intro_tune.mp3")
elif("click this" in text):
    spam = 1
    playsound("scam_1992_intro_tune.mp3")

elif("1000 rs per hours" in text):
    spam = 1
    playsound("scam_1992_intro_tune.mp3")
else:
    spam = 0


if(spam):
    print(" its a spam , stay alert")
    playsound("bachke_rehna_re_baba.mp3")
else:
    print("thankyou so much for your comment!")            

