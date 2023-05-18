import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import datetime

# Initializing NLTK module
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initializing speech recognition and synthesizing......
recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

# Initializing lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define David class
class David:
    def __init__(self):
        self.name = "David"
    
    def listen(self):
        with sr.Microphone() as source:
            print(f"{self.name}: Listening...")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print(f"You: {user_input}")
            self.analyze(user_input)
        except sr.UnknownValueError:
            self.respond("I'm sorry, I couldn't understand you.")
    
    def respond(self, text):
        print(f"{self.name}: {text}")
        synthesizer.say(text)
        synthesizer.runAndWait()
    
    def preprocess_input(self, input_text):
        # Tokenize the input text
        tokens = word_tokenize(input_text.lower())

        # Remove stopwords and lemmatize the remaining words
        preprocessed_tokens = [
            lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stop_words
        ]

        return preprocessed_tokens
    
    def analyze(self, input_text):

        preprocessed_tokens = self.preprocess_input(input_text)

    # Implement logic here
        if "hello" in preprocessed_tokens or "hi" in preprocessed_tokens:
            self.respond("Hello! How can I assist you today?")
        elif "weather" in preprocessed_tokens:
            self.respond("The weather today is sunny and 25 degrees Celsius.")
        elif "time" in preprocessed_tokens:
        # Implement code to get the current time and format it
            current_time = datetime.datetime.now().strftime("%H:%M")
            self.respond(f"The current time is {current_time}.")
        else:
            self.respond("I'm sorry, but I am still learning and cannot provide a meaningful response yet.")

    

# Create an instance of David
David = David()

# Main while loop
while True:
    David.listen()
