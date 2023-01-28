import pyttsx3
import requests  #pip install requests
import speech_recognition as sr
import datetime
import time
import os
import cv2 #pip install opencv-python
from requests import get 
import webbrowser #pip install webbrowser
import pywhatkit as kit #pip install pywhatkit
import smtplib #pip install smtplib
import pyjokes #pip install pyjokes
import wikipedia #pip install wikipedia
import pyautogui #pip install pyautogui



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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('SENDER_MAIL', 'PASSWORD')
    server.sendmail('YOUR_MAIL', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/everything?q=apple&from=2023-01-21&to=2023-01-21&sortBy=popularity&apiKey=YOUR API KEY HERE' #go to newsapi.org, register there and get your api key and write down here

    main_page = requests.get(main_url).json()
    articles = main_page("articles")
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["titles"])
    for i in range(len(day)):
        #print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__=="__main__":
    wishMe()
    while True:

        query = takeCommand()

        if "open notepad" in query:
            speak("ok sir please wait")
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query or "close the notepad" in query:
            speak("as per your order sir, i'm closing the notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open adobe reader" in query:
            speak("ok sir please wait")
            apath = "C:\\Users\\Public\\Desktop\\Adobe Acrobat.lnk"
            os.startfile(apath)

        elif "close adobe reader" in query or "close the adobe reader" in query:
            speak("as per your order sir, i'm closing the adobe reader")
            os.system("taskkill /f /im Acrobat.exe")
        

        elif "open command prompt" in query or "cmd" in query:
            speak("ok sir please wait")
            os.system("start cmd")

        elif "close the cmd prompt" in query or "close the command prompt" in query:
            speak("as per your order sir, i'm closing the cmd prompt")
            os.system("taskkill /f /im cmd.exe")
        

        

        elif "open camera" in query:
            speak("ok sir please wait")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("ok sir please wait")
            music_dir = "C:\Phone\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            speak("ok sir please wait i'm fetching your ip address")
            ip = get('Go to ipify.org').text #to find your IP address go to the ipifi,org and get your api and copy the link of your api key *Note- not copy the api key copy the link and paste here
            speak(f"sir your ip address is {ip}")

        elif "wikipedia":
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            speak(results)
        
        elif "open facebook" in query:
            speak("ok sir please wait")
            webbrowser.open("www.facebook.com")

        elif "send whatsapp message" in query:
            speak("ok sir please wait")
            kit.sendwhatmsg("PHONE NUMBER", "This is a testing message via jarvis AI", 0, 1)
            speak("sir message has been sent")

        elif "open instagram" in query:
            speak("ok sir please wait")
            webbrowser.open("www.instagram.com")
        
        elif "open twitter" in query:
            speak("ok sir please wait")
            webbrowser.open("www.twitter.com")
        
        elif "songs on youtube" in query:
            speak("ok sir please wait i'm playing the songs on you tube")
            kit.playonyt("Heat waves")

        elif "email to somesh" in query:
            speak("ok sir please wait let me setup all things for sending email")
            try:
                speak("sir what should i say")
                content = takeCommand()
                to = "YOUR_MAIL"
                sendEmail(to,content)
                speak("Email has been sent successfully to somesh")

            except Exception as e:
                print(e)
                speak("Sorry sir, something went wrong, i'm not able to sent this email to somesh")


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir i'm fetching the latest news...")
            news()

        elif "shut down the system" in query or "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query or "restart" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.syetem("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        speak("sir do you have any other work")