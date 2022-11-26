import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import pywhatkit.misc as kit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Evening")
    elif hour >= 18 and hour > 0:
        speak("Good Night")
    speak("I am Sanjay, how may i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:

        print("Please say again...")
        return "none"
    return query

def taskexecution():
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open gmail" in query:
            webbrowser.open("mail.google.com")

        elif "open website" in query:
            query = query.replace("open", "")
            query = query.replace("website", "")
            webbrowser.open("https://www.google.com/search?q="+"".join(query))

        elif "play song" in query:
            query = query.replace("play song", "")
            kit.playonyt(query)

        elif "on youtube" in query:
            query = query.replace("on youtube", "")
            kit.playonyt(query)
        
        elif "about the team member" in query:
            speak("Sunny Mishra, Rythem Aggrawal, Sanjay, Suraj Prajapati")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "open vs code" in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open github" in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(codePath)

        elif "open onenote" in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(codePath)

        elif "open word" in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif "open powerpoint" in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        elif "open typing master" in query:
            codePath = "C:\\Program Files (x86)\\TypingMaster11\\TypingMaster.exe"
            os.startfile(codePath)

        elif "sleep now" in query:
            speak("Ok sir, i am going to now sleep you can call me any time.")
            break

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            taskexecution()
        elif "shutdown" in permission:
            speak("Power off")
            sys.exit()

