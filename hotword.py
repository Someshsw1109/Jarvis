import os
import speech_recognition as sr



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
        return "None"
    
    query = query.lower()

    return query

while True:
    wake_up = takeCommand()
    if "wake up" in wake_up:
        os.startfile('C:\\Users\\Somesh Raj\\jarvis proj\\jarvis.py')

    else:
        print("Something went wrong sir please try again......")
