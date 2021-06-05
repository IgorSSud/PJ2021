import datetime
from time import sleep
from Sayer import *
import socket

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
    elif datetime.datetime.today().second == 30:
    #elif "доброе утро" in message:
        sock = socket.socket()
        sock.connect(("localhost", 9090))
        sock.send('hello!'.encode("utf-8"))
        data = sock.recv(1024)
        sock.close()
        print(data.decode('utf-8'))
        sleep(4)
        say_message("Доброе утро сэр")




    else:
        say_message("Я не понимаю о чём вы")
