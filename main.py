import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from yt_auto import *
from news import *
import randfacts

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()
speak('Hello sir i am your assistant. How are you?')

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print('listening...')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "good" or "fine" or "ok" or "about" or "you" and "what" in text:
    speak('I am also having a good day sir.')
    speak('what can i do for you??')      

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print('listening...')
    audio = r.listen(source)
    text2 = r.recognize_google(audio) 
    
if 'information' in text2:
    speak('You need information related to which topic??')
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening...')
        audio = r.listen(source)
        topic = r.recognize_google(audio)
    speak('Searching {} in wikipedia'.format(topic))
    print('Searching {} in wikipedia'.format(topic))

    assist = infow()
    assist.get_info(topic)
elif "news" in text2:
    print('Ok. I will now read the news to you.')
    speak('Ok. I will now read the news to you.')
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
elif 'play' or 'video' in text2:
    speak('You want to play which video?')
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 3.2)
        print('listening...')
        audio = r.listen(source)
        video = r.recognize_google(audio)
    speak('Playing {} on youtube'.format(video))
    print('Playing {} on youtube'.format(video)) 

    assist = music()
    assist.play(video)    
elif 'fact' or 'facts' in text2:
    x=randfacts.get_fact()
    print(x)
    speak("Did you knwow that, " + x )

    