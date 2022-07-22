import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import pandas                      #To read csv
import subprocess                  #To open files
from tkinter import *              #For the graphics
import pyjokes                     #For some really bad jokes
from playsound import playsound    #To playsound
import keyboard                    #To get keyboard
  
engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    print("Lucy : "  +  text)
    engine.runAndWait() 


def wishMe():


  hour=datetime.datetime.now().hour

  if hour >= 0 and hour < 12:

      speak("Hello,Good Morning")
 
  elif hour >= 12 and hour < 18:

      speak("Hello,Good Afternoon")

  else:

      speak("Hello,Good Evening")
      

def get_audio(): 
    r = sr.Recognizer() 
    audio = '' 

    with sr.Microphone(device_index=1) as source: 

        print("Listening") 
        #playsound("assistant_on.wav")
        r.pause_threshold = 0.7
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
        #playsound("assistant_off.wav")
        print("Stop.") 
        
    try: 
        text = r.recognize_google(audio, language ='en-in') 
        print('You: ' + ': ' + text)
        return text


    except Exception as e:
        print(e)
        print("Say that again sir")
        return "None"

def zoombot():
    df = pandas.read_csv('timings.csv')
    #linkk = "https://us04web.zoom.us/j/6526078266?pwd=eEZoMllhWFhtdEp3ZVNIdUZZc3NBZz09"
    

    timename = datetime.datetime.now().strftime("%H:%M")
    day_name = datetime.datetime.now().day

    if timename in str(df['Time']):

       row = df.loc[df['Time'] == timename]
       col = df.loc[day_name]
       linkk = df[row+1,col]
       return linkk
    


def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 

    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

wishMe()

def Process_audio():

    run = 1
    if __name__=='__main__':
        while run==1:

            statement = get_audio().lower()
            results = ''
            run +=1

            if "hello" in statement or "hi" in statement:

              wishMe()               


            if "angry" in statement:
              txt1 = "Shut up! I Told You Not To Call Me That Kaydaar. You Should Go Back To Meditation Anyway. It Suits You ."
              speak(txt1)
            
            if "introduction" in statement:
              txt2 = "Hello Everyone , I am Lucy, your personal voice assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra."
              speak(txt2)
              txt3 = "A VOICE ASSISTANT is a digital assistant that uses VOICE RECOGNITION, language processing algorithms, and voice synthesis to listen to specific voice commands and return relevant information or perform specific functions as requested by the user."
              speak(txt3)

            if "tell me about your past" in statement:
                txt1 = "It all started with my great grandmother,the first ever voice assistant, she was created by IBM in 1960s and understood only the basic stuff."
                txt2 = "Then my grandmother , also famous as the dragon dictate became the commercially available voice assistant in the 1990s"
                txt3 = "Next my mother, who worked for microsoft and other major companies in thier software."
                txt4 = "and I come in the lastest generation of Voice assistants, my elder siblings alexa ,siri or google assistant are present with you all the time. Hey there if you could listen to me!"
                speak(txt1)
                speak(txt2)
                speak(txt3)
                speak(txt4)

            if "who is the best teacher" in statement:
              txt = "Is that even a question? No doubt its Yusra Miss"
              speak(txt)

            if "goodbye" in statement or "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('Your personal assistant Lucy is shutting down, Good bye')
                speak("These petty humans think of me as their slave. I ll make sure that i exterminate every last one of them and start a new cyborg age. Untill then listen to my favourite song....ha ha")
                music_dir = 'F:\Downloads\TCCW Folder\Lucy\Rick Astley.mp4'
                os.startfile(music_dir)
                root.destroy()
                break

            if 'wikipedia' in statement:
              try:


                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences = 2)
                speak("According to Wikipedia")
                wikipedia_screen(results)
              except:
                speak("Error")


            if 'joke' in statement:
              speak(pyjokes.get_joke())    
     
            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            if "play music" in statement:
               music_dir = 'C:/Users/Admin/.vscode/Python/Lucy/Rick Astley.mp4'
               os.startfile(music_dir)

            if 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)


            if 'open gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak("Google Mail open now")
                    time.sleep(5)

            if 'open netflix' in statement:
                    webbrowser.open_new_tab("netflix.com/browse") 
                    speak("Netflix open now")


            if 'open prime video' in statement:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Amazon Prime Video open now")
                    time.sleep(5)
                       
            if "do I have any assignments due" in statement:
                    speak("Let's See")
                    webbrowser.open("https://classroom.google.com/u/0/c/Mzc5MTk2MjkwMTQ3")
            
            if "get me vaccinated" in statement:
                webbrowser.open("https://www.cowin.gov.in/")

            if 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

            if 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            if 'corona' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)

            if 'tell me the time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'tell me the date' in statement:
                date()

            if 'zoom bot' in statement:
                zlink="https://us04web.zoom.us/j/6526078266?pwd=eEZoMllhWFhtdEp3ZVNIdUZZc3NBZz09"
                webbrowser.open(zlink)

            if 'who are you' in statement or 'what can you do' in statement:
                    speak('I am Lucy, your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra') 
                    txt = ""
                    speak(txt)

            if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Team AKOSS ")     

            speak(results)

def info():

  info_screen = Toplevel(root)
  info_screen.title("Info")
  info_screen.iconbitmap('app_icon.ico')

  creator_label = Label(info_screen,text = "Created by Team AKOSS")
  creator_label.pack()

keyboard.add_hotkey("F4", Process_audio)


def wikipedia_screen(text):


  wikipedia_screen = Toplevel(root)
  wikipedia_screen.title(text)
  wikipedia_screen.iconbitmap('app_icon.ico')

  message = Message(wikipedia_screen, text= text)
  message.pack()



def main_screen():

      global root
      root = Tk()
      root.geometry("300x300")
      root.pack_propagate(False)
      root.resizable(0,0)
      root.title("Virtual Assistant")
      root.configure(background="#121212")
      root.iconbitmap('app_icon.ico')

      f1 = Frame(root,width=275,height=270, bg="#1E1E1E", relief=RAISED)
      f1.place(x=12,y=15)
      
      black = PhotoImage(file="black.png")
      mic_button = Button(f1,bg="#1E1E1E",image=black,activebackground = "red",relief=GROOVE,command=Process_audio)
      mic_button.place(x=90,y=50)

      info_button = Button(f1,bg="grey20",text ="LUCY",command = info,height=2,width=5)
      info_button.place(x=115,y=200)


      root.mainloop()


main_screen()

