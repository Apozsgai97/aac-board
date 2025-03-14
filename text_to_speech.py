import pyttsx3

def speak(text):
    if text:
        text = text.lower()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
