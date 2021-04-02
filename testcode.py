                                               # NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    print("Listening test...")
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")

''' Basic - Phase 1 of Jarvis
import speech_recognition as sr
import pyttsx3

print("I'll start...")
engine = pyttsx3.init()
engine.say("Ohh Hello Sir, I am Friday!")
engine.say("Happy to have you here!")
engine.runAndWait()
print("I'm done speaking...")
r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        n=2
        while n:
            n=n-1
            print('listening...')
            voice = r.listen(source)
            print("........ Heared You.........")
            command = r.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                print(command)
                engine.say("Hello Sir!! Have a nice day!")
                engine.runAndWait()
            else:
                engine.say("That's not me!")
                engine.runAndWait()
        #print('Done listening...')
        # command = command.lower()
        # if 'jarvis' in command:
        #     print(command)
except:
    pass
'''