import pyttsx3   
import speech_recognition as sr





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#there is two voices(assistant) already existed in desktops/laptops 'ZIRA', and 'DAVID'
#ZIRA- Female assistant
#DAVID- Male assistant
