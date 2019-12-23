import os
import time
import random
import playsound
import webbrowser
from gtts import gTTS
import speech_recognition as sr

# Create an object
r = sr.Recognizer()


def record_speech(question=""):
    # Use microphone as speech source
    with sr.Microphone() as source:
        if question:
            speak(question)

        speech = r.listen(source)
        speech_text = ""

        try:
            speech_text = r.recognize_google(speech)
        except sr.UnknownValueError:
            speak("Sorry, I Could Not Understand What You Have Just Said.\n")
        except sr.RequestError:
            speak(
                "Sorry, I Could Not Connect To The Internet. Resolve The Issue And Come Back.")

        return speech_text


def speak(speech_text):
    tts = gTTS(speech_text, lang="en")
    
    random_number = random.randint(1, 1000)
    audio_file = "speech-" + str(random_number) + ".mp3"
    
    tts.save(audio_file)
    playsound.playsound(audio_file)
    
    print(speech_text)
    os.remove(audio_file)


def respond_to_speech(speech_text):
    if "what time is it" in speech_text:
        speak("Oh My Goodness! This Is What You Have Just Asked For:\n")

        speak(time.ctime())

    if "find location" in speech_text:
        location = record_speech("What is the location?")

        url = "https://google.com/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)

        speak("The location " + location + " has been found.")

    if "exit" in speech_text:
        exit()


time.sleep(1)

speak("Tell Me What You Would Like To Do And I Will Do It For You.\n")

while 1:
    speech_text = record_speech()

    respond_to_speech(speech_text)
