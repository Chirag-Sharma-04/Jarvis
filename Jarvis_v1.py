import speech_recognition as sr
import webbrowser as wb
import pywhatkit
import pyttsx3
import datetime 
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def alarm(c):
    i = 1
    talk('alarm set for '+c)
    while True:
        time = datetime.datetime.now().strftime('%I%M')
        ctime = datetime.datetime.now().strftime('%I:%M %p')
        if time == c:
            break
    talk('the time is ' + ctime)
    print('over')


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:

    print('speak now')
    talk(' I am online ')
    audio=r3.listen(source)
    command=r2.recognize_google(audio)
    print(command)


if 'demo' in command:#demo
    r2 = sr.Recognizer()

    try:
        talk('hello, my name is jarvis... i am your  personal assistant...what can i do for you ')
    except sr.UnknownValueError:
        print('error')



if 'open YouTube' in command:#yt
    r2 = sr.Recognizer()
    url='https://www.youtube.com/'

    try:
        wb.get().open_new(url)
        talk('opening youtube')
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'time' in command:#time
    r2 = sr.Recognizer()
    time = datetime.datetime.now().strftime('%I:%M %p')

    try:
        talk('Currently the  time is ' + time)
    except sr.UnknownValueError:
        print('error')

if 'weather' in command:#weather
    r2 = sr.Recognizer()
    url='https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57.1851j0j7&sourceid=chrome&ie=UTF-8'

    try:
        wb.get().open_new(url)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'search' in command:#search
    r2 = sr.Recognizer()
    url='https://www.google.com/search?q='
    s = r2.recognize_google(audio).replace("open Google and search for", '')
    print(s)

    try:
        talk('searching for '+s)
        wb.get().open_new(url+s)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'play' in command:#music
    r2 = sr.Recognizer()
    song = r2.recognize_google(audio).replace('play', '')
    talk('playing '+song)

    try:
        pywhatkit.playonyt(song)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'alarm' in command: #alarm
    r2 = sr.Recognizer()
    o = r2.recognize_google(audio).replace("set an alarm for ", '')
    print(o)
    if ':' in o:
        s=o.replace(":",'')
        s= s.replace("o'clock", '')
        s=s.replace(" ",'')
        t = '0' + str(s)
        print('hello')
        print(t)
        c=t
        alarm(c)
    else:
        s = o.replace("o'clock", '00')
        s = s.replace(" ", '')
        print(s)
        int(s)
        if(int(s)<1000):
            t = '0' + str(s)
            print(t)
            c=t
            alarm(c)