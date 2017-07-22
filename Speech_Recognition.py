import speech_recognition as sr
import pyttsx3
from phue import Bridge

# put your Bridge ip like this 192.168.0.2
b = Bridge("192.168.0.2")

# pyttsx3 speech to text engine
engine = pyttsx3.init()
engine.setProperty('rate', 120) #how farst it talk
engine.say("Hello")  #what it need to say
engine.runAndWait()  #runAndWait it is stopper so it ready for new word to say

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    rec = r.recognize_google(audio, language = "en-US")  # this so we use google speech_recognition
    try:
        print(rec)
        if rec == "light on":
            b.set_light(7,'on', True)    # b.set_light(light,'on', True)
        elif rec == "light off":
            b.set_light(7,'on', False)   # trun the light off
    except sr.UnknownValueError:         # if the speech_recognition dont understand/don't the know the word
        engine.say("Sorry, What")
        engine.runAndWait()
