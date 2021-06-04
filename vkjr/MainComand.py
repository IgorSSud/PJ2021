from time import sleep
import datetime

import AudioQuery
from Sayer import *
import asyncio
from AudioQuery import *


def do_this_command(message):
    try:
        message = message.lower()
    except:
        print(message)
        if message == None:
            return 0
    if "привет" in message or "Приветик" in message:
        say_message("Привет ")

    # ---------------------------------------------
    elif "как дела" in message:
        say_message("Лучше чем у тебя")
        sleep(4)
        say_message("Придурок")
    # ---------------------------------------------

    elif "пока" in message:
        say_message("Пока пока")
        exit()
    # elif datetime.datetime.today().hour == 5:
    elif "доброе утро" in message:

        say_message("Доброе утро сэр")


    else:
        say_message("Я не понимаю о чём вы")
