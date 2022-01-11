import pyttsx3 # pip install pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime

import wikipedia
import webbrowser
import os
import smtplib, ssl
import requests, json

print("Initializing RUSH")
MASTER = "Siam"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# Speak function will speak/Pronounce the given string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# It will wish as per the current time
def wish_Me():
    hour = int(datetime.datetime.now().hour)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)

    if hour>=6 and hour <12:
        speak("Good Morning " + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon " + MASTER)

    elif hour>=18 and hour<20:
        speak("Good Evening " + MASTER)
    else:
        speak("Good Night " + MASTER)
    
    speak("I am your Virtual assistant RUSH. How can I help you?")

def output(out):
    # print(out)
    engine.say(out)
    engine.runAndWait()

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

# Defining the email function
def sendEmail(to, content):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = input("Type sender email and press enter:")
    password = input("Type sender password and press enter:")

    # Create a secure SSL context
    context = ssl.create_default_context()

    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, to, content)

# Main program starting
def main():
    speak("Initializing Rush...")
    wish_Me()
    query = takeCommand()

    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        #query = query.replace("wikipedia", "")
        query = takeCommand()
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open('youtube.com')
        output("what you want to search on YouTube?")
        pywhatkit.playonyt(takeCommand())
        

    elif 'open facebook' in query.lower():
        # webbrowser.open('facebook.com')
        url = "facebook.com"
        webbrowser.open_new_tab(url)

    elif 'open linkedin' in query.lower():
        # webbrowser.open('linkedin.com')
        url = "https://www.linkedin.com/feed/"
        webbrowser.open_new_tab(url)

    elif 'open github' in query.lower():
        # webbrowser.open('github.com')
        url = "https://github.com/siamkhanra"
        webbrowser.open_new_tab(url)

    elif 'open google' in query.lower():
        # webbrowser.open('google.com')
        output("What you want to search")
        webbrowser.open("https://www.google.com/search?q="+takeCommand())

    elif 'send a whatsapp message' in query.lower():
        phone_no = input("Type phone number and press enter:")
        speak("What should I send to that person?")
        content = takeCommand()
        pywhatkit.sendwhatmsg(phone_no,content,1,53)
        print("Sending Whatsapp Message")
        speak("Sent Whatsapp Message")

    elif 'play music' in query.lower():
        songs_dir = "E:\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'open image' in query.lower():
            image_dir = "E:\Picture"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")
        print(strTime)

    elif 'the date' in query.lower():
        output("Current date is " + str(datetime.datetime.now().day) + " " +
               str(datetime.datetime.now().month) + " " + str(datetime.datetime.now().year))

    elif 'open code' in query.lower():
        codePath = "D:\Course\ICE all course\ICE 475 Artificial Intelligence & Expert Systems\Project\Task1.py"
        os.startfile(codePath)


    elif 'send email' in query.lower():
        try:
            speak("What should I send to that person?")
            content = takeCommand()
            to = input("Type recevicer email and press enter:")
            sendEmail(to, content)
            speak("Email has been sent to the receiver")
            
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to send this email to that person.") 

main()


