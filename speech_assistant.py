import speech_recognition as sr

# Create an object
r = sr.Recognizer()

def record_speech():
    # Use microphone as speech source
    with sr.Microphone() as source:
        speech = r.listen(source)
        speech_text = ""

        try:
            speech_text = r.recognize_google(speech)
            print("Oh My Goodness! This Is What You Have Just Said:\n")
        except sr.UnknownValueError:
            print("Sorry, I Could Not Understand What You Have Just Said.\n")
        except sr.RequestError:
            print("Sorry, I Could Not Connect To The Internet. Resolve The Issue And Come Back.")

        return speech_text


print("Tell Me What You Want And I Will Write It Down For You.\n")
speech_text = record_speech()

print(speech_text)
