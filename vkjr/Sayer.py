import os
import time
import pyglet
import requests
from requests import post, Session
from fake_useragent import UserAgent

def synthesize(folder_id, iam_token, text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Bearer ' + iam_token,
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        'folderId': folder_id,
        'voice': 'filipp'
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:

            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk

def say_message(message):
    name="speech"+str(time.time())+".ogg"
    with open(name, "wb") as f:
        for audio_content in synthesize("b1gcostvk9b3su7hcj0p",
                                        set_token(),
                                        message):
            f.write(audio_content)
    f.close()
    song = pyglet.media.load(name)
    song.play()
    os.remove(name)

def set_token():

    response =requests.post(url="https://iam.api.cloud.yandex.net/iam/v1/tokens",data="{\"yandexPassportOauthToken\":\"AQAAAAAQSILGAATuwaMCfX7vUkhSr4jOs0Fa_Do\"}")
    return response.json()["iamToken"]

def Auth_Ya():


    link = "https://passport.yandex.com/auth"

    user = UserAgent().random

    headers = {
        'user-agent': user
    }

    data = {
        'login': 'votelineage22',
        'passwd': 'Jarvis2020',
    }

    session = Session()

    responce = session.post(link, headers=headers, data=data)

    with open("responce.html", "w") as file:
        file.write(responce.text)


