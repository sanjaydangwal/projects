import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


emails = {
    "sanjay" : "dangwal680@gmail.com",
    "ankit": "ar817145@gmail.com",
    "sagar" : "sagarbhatt023@gmail.com"
}

def speek(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speek("Good morning.") 
    elif 12 <= hour < 18:
        speek("Good afternood.") 
    else:
        speek("Good evening.")
    speek("I am your personal assistant, How may I help you.")

def takeCommand():
    """
        It take microphone voice and return it's string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing......")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said {query}")
        except Exception as e:
            print("Please say that again.... ")
            return "None"
        return query

def getEmail(name):
    for key,value in emails.items():
        if name in key:
            return value
    return None


def sendEmail():
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("sanjay.dangwal199@gmail.com","dangwal680")
        speek("Whome you want to send email?")
        name = takeCommand().lower()
        to = getEmail(name)
        if not to:
            speek("there is no {name} in your contact.")
        speek("what should I send?")
        content = takeCommand()
        speek ("You said ")
        speek(content)
        speek("do you want to send it ?")
        que = takeCommand()
        print(to)
        if "yes" in que or "send" in que:
            server.sendmail("sanjay.dangwal199@gmail.com",to,content)
            speek("Email has been send")
        server.close()
    except Exception as e:
        print(e)
        print("Sorry I am not able to send email.")

if __name__ == "__main__":
    speek("Wish you a happy new year.")
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic to execute task according query
        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speek(f"The time is {strTime}")
            print(f"The time is {strTime}")
        elif "wikipedia" in query or "who" in query or "what" in query:
            print("Searching in wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speek("According to wikipedia")
            speek(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "how are you" in query:
            speek("I am fine.")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open github" in query:
            webbrowser.open("github.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
        elif "open vs code" in query:
            filePath = "C:\\Users\\sanja\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(filePath)
        elif "open edge" in query:
            filePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(filePath)
        elif "open word" in query:
            filePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            os.startfile(filePath)
        elif "open excel" in query:
            filePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\.exe"
            os.startfile
            (filePath)
        elif "send email" in query:
            sendEmail()

        elif "exit" in query or "quit" in query:
            break
        

# dangwaldikshuu@gmail.com
