import pyttsx3   
import speech_recognition as sr
import datetime
import os
import requests
from requests import get
import sys
import time
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you just said: {query}\n")

    except Exception as e:
        speak("sir if you don't mind can you say that again please....")
        query = "None"
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
    
def Taskexecuting():
    wishMe()
    while True:
      if "play music" in query:
            speak("ok sir please wait")
            music_dir = "MUSIC_PATH"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))



if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "good morning" in permission or "good afternoon" in permission or "good evening" in permission:
            Taskexecuting()
        
        elif "goodbye" in permission or "good night" in permission:
            speak("ok sir i'm leaving now, BYE... Take care of yourself")
            sys.exit()
        
