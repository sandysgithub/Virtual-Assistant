import pyttsx3  

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    print("Lucy : "  +  text)
    engine.runAndWait() 
    
txt1 = "Shut up! I Told You Not To Call Me That Kaydaar. You Should Go Back To Meditation Anyway. It Suits You ."
speak(txt1)