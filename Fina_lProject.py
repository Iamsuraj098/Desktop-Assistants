import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import pywhatkit.misc as kit
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("450x450")
root.title("Mini Project")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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


class task:

    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak("Good Morning Sir")
        elif hour > 12 and hour < 18:
            speak("Good Evening Sir")
        elif hour >= 18 and hour > 0:
            speak("Good Night Sir")
        print("I am Sanjay, how may i help you")
        speak("I am Sanjay, how may i help you")

    def taskexecution(self):
        speak("give command")
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
                webbrowser.open(
                    "https://www.google.com/search?q="+"".join(query))

            elif "play song" in query:
                query = query.replace("play song", "")
                kit.playonyt(query)

            elif "on youtube" in query:
                query = query.replace("on youtube", "")
                kit.playonyt(query)

            elif "who is in the team" in query:
                print("Sunny Mishra, Rlythem Aggrawal, Suraj Prajapati and Sanjay")
                speak("Sunny Mishra, Rythem Aggrawal, Suraj Prajapati and Sanjay")

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {strTime}")
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
                print("Ok sir, i am going to now sleep you can call me any time.")
                speak("Ok sir, i am going to now sleep you can call me any time.")
                break


call_a = task()


class GUI:

    def head(self):
        frame0 = tk.Frame(root, borderwidth=20, bg="grey", relief=tk.SUNKEN)
        frame0.pack(side=tk.TOP, pady=12, padx=12, fill=tk.X)
        # heading
        head = tk.Label(frame0, text="SANJAY - DESKTOP ASSISTANT",
                     font="comicsansms 30 bold", bg="grey", fg="white")
        head.pack()

    def wakeup(self):
        frame2 = tk.Frame(root, borderwidth=8, bg="grey", relief=tk.SUNKEN)
        frame2.pack(side=tk.LEFT, anchor=tk.SW, pady=12, padx=12)
        Wake_up = tk.Button(frame2, text="Wake Up",
                         font="comicsansms 20 bold", command=call_a.wishme)
        Wake_up.pack(anchor=tk.NW)

    def taskperform(self):
        frame2 = tk.Frame(root, borderwidth=8, bg="grey", relief=tk.SUNKEN)
        frame2.pack(side=tk.LEFT, anchor=tk.SW, pady=12, padx=12)
        Wake_up = tk.Button(frame2, text="Commands",
                         font="comicsansms 20 bold", command=call_a.taskexecution)
        Wake_up.pack(anchor=tk.NW)

    def shutdown(self):
        frame3 = tk.Frame(root, borderwidth=8, bg="grey", relief=tk.SUNKEN)
        frame3.pack(side=tk.RIGHT, anchor=tk.SW, pady=12, padx=12)
        Shutdowm = tk.Button(frame3, text="Shutdown",
                          font="comicsansms 20 bold", command=sys.exit)
        Shutdowm.pack()

call_b = GUI()
call_b.head()

img = Image.open("E:\\programming\\python\\desktop Assistant.png")
photo = ImageTk.PhotoImage(img)
dp = tk.Label(root, image=photo)
dp.pack(side=tk.TOP, pady=12, padx=12)

call_b.wakeup()
call_b.taskperform()
call_b.shutdown()

root.mainloop()
