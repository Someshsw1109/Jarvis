# In the jarvis command python file you can see that i used if statement as
# if __name__ == "__main__" but now here we add one more command wake up jarvis
# for this you have to replace the if __name__  == "" statement with def executing(): and write the given code in last line of your jarvis python file
import pyttsx3
import speech_recognition as sr
import datetime
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
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


def executing():
    wishMe()
    while True:

        query = takeCommand()
        if "nothing" in query:
            speak("sir can you say again")

        # write your own code and also make your own command here

        #----------- code here

        #----------- code here



        # ----------- code here


if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "good morning" in permission or "good afternoon" in permission or "good evening" in permission:
            executing()