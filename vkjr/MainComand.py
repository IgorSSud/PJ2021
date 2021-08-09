import datetime
from time import sleep
from Sayer import *
import socket
import datetime
import webbrowser
import wikipedia
def AC_DC_Shoot_still():

    say_message("Выполняю сэр")
    sock = socket.socket()
    sock.connect(("localhost", 9091))
    sock.send('AC_DC_Shoot_still'.encode("utf-8"))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))
    print("Play AC\DC-Shoot still")
def Weather():

    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=fd7a000568216df01e6907e2b727ef63")
    data_json = response.json()
    cels = round(data_json["main"]["feels_like"] -273)
    print(cels)

    say_message(" На улице температура" + str(
        cels) + " градусов цельсия.Лёгкая облачность.")
    sleep(2)
def Wikisearch(message_search):
    wikipedia.set_lang('ru')
    message_search = message_search.replace('что такое ','')
    ny = wikipedia.search(message_search, results=1, )

    text = wikipedia.summary(ny[0])
    return text
def do_this_command(message):
    try:
        message = message.lower()
    except:
        print(message)
        if message == None:
            return 0
    if "привет" in message or "Приветик" in message:
        say_message("Привет")
        sleep(0.2)

    # ----------FUNCKTION_COMMAND-----------------
    elif "как дела" in message:
        say_message("Лучше чем у тебя")
        sleep(4)
        say_message("Придурок")
    elif "время" in message:
        say_message("Сейчас время " + str(datetime.datetime.today().hour)+"Часов " +str(datetime.datetime.today().minute)+"Минут")
        print("Сейчас время " + str(datetime.datetime.today().hour)+"Часов " +str(datetime.datetime.today().minute)+" Минут")
        sleep(2)
    elif "погода" in message:
        Weather()
    elif "что такое" in message:
        print(Wikisearch(message))
        say_message(Wikisearch(message))
    # ----------MUSIC_COMMAND-----------------
    elif "ac dc" == message:
        print(1)
        try:
            AC_DC_Shoot_still()
        except:
            say_message("Сэр произошла ошибка.Я не смог подключиться к плэеру.")
    elif "радио" == message:
        print("Radio")
        say_message("Выполняю")
        url= "https://www.youtube.com/watch?v=hLXZ2RbGO1g&ab_channel=IxoMusic"
        webbrowser.open(url)
    elif "pendulum" in message:
        say_message("Выполняю")
        url = "https://youtu.be/y013oCa6WAQ?t=1"
        webbrowser.open(url)

    # -------------EXIT_COMMAND--------------------

    elif "пока" in message:
        say_message("Пока пока")
        sleep(3)
        exit()






