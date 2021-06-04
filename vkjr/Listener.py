import speech_recognition as sr


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("скажи команду")
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio,language="ru")
        print("Вы сказали :" + our_speech)
        return our_speech
    except:
        print("pass")
        pass
