import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


def takeCommand():
    """it takes microphone input from the user and return string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    SENDER_EMAIL = 'YOUR EMAIL ADDRESS'
    SENDER_PASSWORD = 'YOUR EMAIL PASSWORD'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, to, content)
    server.close()


if __name__ == "__main__":
    # speak("hello satyam")
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "MUSIC FOLDER PATH"
            songs = os.listdir(music_dir)
            # print(songs)
            randNum = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[randNum]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif "open code" in query:
            codePath = r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'email to satyam' in query:
            try:
                RECEIVER_EMAIL = 'RECEIVER EMAIL ADDRESS'
                speak("What should I say?")
                content = takeCommand()
                to = RECEIVER_EMAIL
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Satyam! I am not able to send this email.")
        
        elif query == 'quit':
            speak("See you soon!")
            exit()
                
