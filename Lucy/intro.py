
import pyttsx3  

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    print("Lucy : "  +  text)
    engine.runAndWait() 

txt2 = "Hello Everyone , I am Lucy, your personal voice assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra."
speak(txt2)
txt3 = "A VOICE ASSISTANT is a digital assistant that uses VOICE RECOGNITION, language processing algorithms, and voice synthesis to listen to specific voice commands and return relevant information or perform specific functions as requested by the user."
speak(txt3)