import pyttsx3  

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    print("Lucy : "  +  text)
    engine.runAndWait() 

txt1 = "It all started with my great grandmother,the first ever voice assistant, she was created by IBM in 1960s and understood only the basic stuff."
txt2 = "Then my grandmother , also famous as the dragon dictate became the commercially available voice assistant in the 1990"
txt3 = "Next my mother, who worked for microsoft and other major companies in thier software."
txt4 = "and I come in the latest generation of Voice assistants, my elder siblings alexa ,siri or google assistant are present with you all the time. Hey there if you could listen to me!"
speak(txt1)
speak(txt2)
speak(txt3)
speak(txt4)