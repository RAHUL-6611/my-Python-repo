# works only when internet is on
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('')
alexa = sr.Recognizer()
# try:
#     with sr.Microphone() as source:
#         print("listening...")
#         voice = alexa.listen(source)
#         command = alexa.recognize_google(voice, language='en-in')
#         print(command)

# except Exception as e:
#     print("no")
#     print(e)