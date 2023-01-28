import pyttsx3   
import speech_recognition as sr





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate', 100) #(this is the code for speech rate control)
#for voice in voices:
   # print(voice.id)
   # engine.setProperty('voice', voice.id)
   # engine.say("hello sir i'm your virtual assistant")
#engine.runAndWait()