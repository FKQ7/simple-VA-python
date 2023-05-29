import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

            return command
    except:
        return None


def run_alexa():
    command = take_command()
    if command  is not None:
        print(command)
        
        if 'play on' in command:
            pywhatkit.playonyt("quran")
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        
        elif 'send me a message' in command: #sending via whatsup
            pywhatkit.sendwhatmsg("+966530844303", "Hi", time, time )

        elif 'look for' in command:
            search = command.replace('look for', '')
            talk('look for' + search)
            pywhatkit.search(search)
        
        elif 'saudi arabia' in command:
            saudi_arabia = "saudi arabia"
            talk('look for' + saudi_arabia)
            pywhatkit.search(saudi_arabia)
        
        elif 'play on' in command:
            pywhatkit.playonyt("quran")
        
        elif 'play quran' in command:
            pywhatkit.playonyt("quran")
        
        elif 'play music' in command:
            music = command.replace('play', '')
            talk('playing ' + music)
            pywhatkit.playonyt(music)

        elif






        else:
            talk('Please say the command again.')


while True:
    run_alexa()