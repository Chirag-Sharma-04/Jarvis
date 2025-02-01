import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def Convert(string):  # converts string to list
    li = list(string.split(" "))
    return li

a=input("Enter the Paragraph : ")

b=Convert(a)

#print(b)

for x in b:
    print(x)
    talk(x)
    time.sleep(0.5)