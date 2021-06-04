import asyncio

import pyttsx3


def say_message(message):
    tts = pyttsx3.init()
    voices = tts.getProperty("voices")
    tts.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Pavel")
    tts.say(message)
    tts.runAndWait()
