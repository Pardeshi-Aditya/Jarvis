import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

print("Running Jarvis...")
engine = pyttsx3.init()
r = sr.Recognizer()

# Defining talk function to make Jarvis speak
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
# Welcome :
talk("Ohh hello sir, Happy to have you here!")
# taking voice command, converting it to text and returning it
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            print("........ Heared You.........")
            command = r.recognize_google(voice) # using google api for voice recognition
    except:
        print("Couldn't access Microphone...")
    return command

def run_jarvis():
    works = 0 # To define if Jarvis was able to provide some service or not
    # Infinite Loop for taking commands back to back unless Jarvis is asked to terminate
    while True:
        command = take_command()
        print(command)
        if 'friday' or 'jarvis' or 'Hi jarvis' in command:
            command = command.replace('jarvis' and 'friday', '')

        # Different functions by Jarvis:

        if 'play' in command:
            works=1 # this command was fired
            song = command.replace('play','')
            talk('Playing ' + song + " on YouTube")
            pywhatkit.playonyt(song)
            break
        if 'time' in command:
            works = 1  # this command was fired
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"It's {time} now")
        elif 'who is' or 'tell me about' in command:
            works=1 # this command was fired
            person = command.replace('who is' and 'tell me about','')
            info = wikipedia.summary(person,1)
            talk(info)
        elif 'joke' or 'jokes' in command:
            works =1 # this command was fired
            talk(pyjokes.get_joke())
        # Keep commands above this line...
        # Here the exit and exception handling is written
        elif 'terminate' in command:
            works = 1  # this command was fired
            talk("Okay! I'll take your leave sir...")
            break
        if works == 0:
            talk("Couldn't get that sir...Please try again...")
            continue
        talk("What else can I do for you sir?")

# Running Jarvis -
run_jarvis()
