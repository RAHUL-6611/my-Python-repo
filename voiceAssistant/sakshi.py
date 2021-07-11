import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import pywhatkit as kit

engine = pyttsx3.init('sapi5')  # api for voices by microsoft
voices = engine.getProperty('voices')  # gets inbuild voives for you
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)  # sets the voice
# exit()



def speak(input):
    engine.say(input)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if 4 <= hour < 12:
        speak("Good Morning!, Raahool Sir")

    elif 12 <= hour < 16:
        speak("Good afternoon!, Raahool Sir")

    elif 16 < hour <= 20:
        speak("Good evening!, Raahool Sir")

    else:
        speak("Good Night!, Raahool Sir")

    # speak("Hello Sir, i am Saaakshi, How i can help you sir!")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        input = r.listen(source)
        

    try:
        print("Recognizing ....")
        query = r.recognize_google(input, language='en-in')
        print(query)
        # print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    
    return query


if __name__ == "__main__":
    # speak("Hello Raahool Sir, What can I do for you!")
    # wishme()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia")
            query = query.replace("wikipedizza", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            print(results)
            speak(results)
            

    