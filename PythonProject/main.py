import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)


def speak(command):
    engine.say(command)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("you Said.......")
        print("Command =  " + r.recognize_google(audio, language='en-in'))
    except Exception as e:
        print("Please try again later")

command()
