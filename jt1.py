import datetime



from sys import platform

import pyttsx3





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




if __name__ == '__main__':
    query = takeCommand().lower()
    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif 'list' in query:
            speak("what is your to do list")
            text = takeCommand()
            now = datetime.datetime.now()
            now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
            text_file = open("Todo Lists\\Todolist{}.txt".format(now_str), "w")
            text_file.write(text)
            text_file.close()
