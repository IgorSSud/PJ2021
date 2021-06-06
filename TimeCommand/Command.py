import datetime
import socket
from time import sleep
from Sayer import say_message
import requests

morning_command_counter = 0


def Time_command():
    global morning_command_counter
    print("Time => " + str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(
        datetime.datetime.today().second) + "  |  Morning counter => " + str(morning_command_counter))

    try:
        # if datetime.datetime.today().hour == 9 and datetime.datetime.today().minute == 0 and morning_command_counter == 0:
        if datetime.datetime.today().second == 10:
            sock = socket.socket()
            sock.connect(("localhost", 9090))
            sock.send('Morning'.encode("utf-8"))
            data = sock.recv(1024)
            sock.close()
            morning_command_counter = morning_command_counter + 1
            print(data.decode('utf-8'))
            sleep(6)

            response = requests.get(
                "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=fd7a000568216df01e6907e2b727ef63")
            data_json = response.json()
            cels = round(data_json["main"]["feels_like"] / 15.5)
            print(cels)

            say_message("Доброе утро сэр , время " + str(
                datetime.datetime.today().hour) + " утра на улице пасмурно температура" + str(cels) + "цельсия")
        elif datetime.datetime.today().hour == 22 and datetime.datetime.today().minute == 0 and morning_command_counter == 1:
            morning_command_counter = 0

    except:
        print(datetime.datetime.today().second)
    sleep(0.5)
