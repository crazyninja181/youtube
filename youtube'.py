import speech_recognition as sr 
import pyttsx3
import pywhatkit as kit
def speak(text):
    eng=pyttsx3.init()
    voices=eng.getProperty("voices")
    eng.setProperty("voice",voices[1].id)
    eng.say(text)
    eng.runAndWait()
    eng.stop()
def listen():
    r=sr.Recognizer()
    text=None
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.1)
        speak('listening now')
        audio=r.listen(source)
    try:
        speak("recognizing")
        text=r.recognize_google(audio,language="hi-IN")
        speak("you said"+text)
        return text
    except:
        speak("couldnot understand audio")
speak("enter song name")
audio=listen()

if audio:
    kit.playonyt(audio)