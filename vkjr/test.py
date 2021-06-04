import asyncio
import threading
import pyttsx3
from playsound import playsound

from Sayer import say_message


def a():
    pass


def b(message):
    tts = pyttsx3.init()
    voices = tts.getProperty("voices")
    tts.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Pavel")
    tts.say(message)
    tts.runAndWait()
def c():
    i=0
    while i<10:
        print(i)
        i=i+1


def d():
    i = 10
    while i < 20:
        print(i)
        i = i + 1


threading.Thread(target=d()).start()
threading.Thread(target=c()).start()
