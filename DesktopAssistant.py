import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from plyer import notification


admin = "ANURAG SIR"
print("Running some features  .. . . ")

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)

    if(hour>=0 and hour<=12):
        speak("GOOD MORNING" + admin)
    elif(hour>12 and hour<16):
        speak("GOOD AFTERNOON" + admin)
    elif(hour>=16 and hour<20):
        speak("GOOD EVENING" + admin)
    else:
        speak("GOOD NIGHT")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . . . ")
        command = r.listen(source)

        try:
            print("RECOGNIZING COMMAND")
            query = r.recognize_google(command, language='en-in')
            print(query)

        except Exception as e:
            print("something went wrong try again!")

    return query


while 1:
    st = time.time()
    speak('STARTING DESKTOP ASSISTTANT' + admin)
    greet()
    query = listen().lower()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    elif 'who' and 'you' in query:
        speak("I AM A SIMPLE DESKTOP ASSISTANT DESIGNED AND DEVOLOPED BY SIR  ANURAG JOSHI PRIAVTE LIMITED")
    elif 'open youtube' in query:
        webbrowser.get(chrome_path).open("youtube.com")
    elif 'open mail' in query or 'open email' in query:
        webbrowser.get(chrome_path).open("gmail.com")
    elif 'open c drive' in query:
        os.startfile("C:")
    elif 'open d drive' in query:
        os.startfile("D:")
    elif 'tell' and 'time' in query or 'what' and 'time' in query:
        speak("It's " + datetime.datetime.now().strftime("%H:%M:%S"))
    et = time.time()
    if et-st>=1200:
        notification.notify(title="ITS TIME FOR 20-20-20!!", message="LOOK 20 FEET AWAY FOR 20 SECONDS IN EVERY 20 MINUTES!!", timeout=5)
