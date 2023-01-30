import pyttsx3   
import speech_recognition as sr
import datetime
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("sir if you don't mind can you say that again please....")
        return "None"
    
    query = query.lower()

    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good Morning, its {tt} sir")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon, its {tt} sir")
    else:
        speak(f"Good Evening, its {tt} sir")
    speak("Hey sir i am jarvis, Please tell me how may i help you")
