import datetime
import getpass
import os
import smtplib
import sys
import webbrowser
from sys import platform
import random
import psutil
import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia


from diction import translate
from loc import weather
from news import speak_news, getNewsUrl
from youtube import youtube

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# print(voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")

    else:
        speak('Good Evening Boss')


    speak('JUSTINE here. Is there any work for me?')



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'Wrok to do: {query}\n')

    except Exception as e:
        # print(e)
        speak('Please, say that again')
        print('Please, say that again')
        return 'None'
    return query




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def screenshot():
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    outFile = pyautogui.screenshot('C:\\Users\\BeingMF\\Pictures\\JustineImageFile{}.PNG'.format(now_str))


if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        if 'justine are you there' in query:
            speak("Yes Boss, at your service")

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'spotify' in query:
            print('opening spotify')
            speak('opening Spotify')
            webbrowser.get('chrome').open_new_tab('https://open.spotify.com')

        elif 'weather' in query:
            weather()

        elif 'cpu' in query:
            cpu()

        elif 'hello' in query:
            speak("Hello there, nice to meet you")

        elif 'hii' in query:
            speak("Hello there, nice to meet you")

        elif 'hi' in query:
            speak("Hello there, nice to meet you")


        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)


        elif 'your developer' in query:

            if platform == "win32" or "darwin":

                list1 = ['Prateek, and Anshul are my masters', 'Anshul and Prateek created me, those are my matsers',
                        'Prateek, and anshul are my master. For me, they are GOD', 'Anshul and Prateek']

                list2 = random.choice(list1)

                speak(list2)

            elif platform == "linux" or platform == "linux2":

                name = getpass.getuser(list2)

                speak(name, 'is my master. He is running me right now')


        elif 'your name' in query:
            speak('My name is Justine. I am your A I assistant system')

        elif 'calculator' in query:
            os.system('py calc.py')

        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\BeingMF\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'who are you' in query:
            speak('My name is Justine. I am an A I assistant system')

        elif 'why are you' in query:
            speak('I am here to serve you')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/pratikdaherwal')

        elif 'my website' in query:
            speak('opening your website in google chrome')
            webbrowser.get('chrome').open_new_tab(
                'https://pratikdaherwal.github.io/')


        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            speak("Exiting now")
            sys.exit()

        elif 'exit' in query:
            speak("Exiting now")
            sys.exit()

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())



        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'email to Anshul' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'email'
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                speak('Sorry sir, Not able to send email at the moment')

    