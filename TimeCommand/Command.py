import datetime
import socket
from time import sleep
from Sayer import say_message
import requests

morning_command_counter = 0
tablet_command_counter = 0
tablet_01_command_counter = 0
def Morning_at_8_50():
    sock = socket.socket()
    sock.connect(("localhost", 9091))
    sock.send('Morning'.encode("utf-8"))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))
    sleep(25)

    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=fd7a000568216df01e6907e2b727ef63")
    data_json = response.json()
    cels = round(data_json["main"]["feels_like"] -273)
    print(cels)

    say_message("Доброе утро сэр . Время " + str(
        datetime.datetime.today().hour) + "часов утра. На улице температура" + str(
        cels) + " градусов цельсия.Лёгкая облачность. Сегодня много задач.")
    sleep(20)
    say_message("Незабудте выпить протэин и витамины.")

def Time_command():
    global morning_command_counter
    global tablet_command_counter
    global tablet_01_command_counter
    print("Time => " + str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(
        datetime.datetime.today().second) + "  |  Morning counter => " + str(morning_command_counter))

    try:
        if datetime.datetime.today().hour == 16 and datetime.datetime.today().minute == 45 and morning_command_counter == 0:
        #if datetime.datetime.today().second/10 == 0:
            Morning_at_8_50()
            morning_command_counter = morning_command_counter + 1

        elif datetime.datetime.today().hour == 10 and datetime.datetime.today().minute == 0 and tablet_command_counter == 0:
            say_message("Сер время "+str(datetime.datetime.today().hour)+"часов .Выпейте пожалуйста витамины.")
            tablet_command_counter=tablet_command_counter+1

        elif datetime.datetime.today().hour == 22 and datetime.datetime.today().minute == 0 and tablet_01_command_counter == 0:
            say_message("Сер время "+str(datetime.datetime.today().hour)+"часа .Выпейте пожалуйста витамины.")
            tablet_01_command_counter=tablet_01_command_counter+1

        elif datetime.datetime.today().hour == 22 and datetime.datetime.today().minute == 0 and morning_command_counter == 1:
            morning_command_counter = 0
            tablet_01_command_counter = 0
            tablet_command_counter = 0
    except:
        print(datetime.datetime.today().second)
    sleep(0.5)
