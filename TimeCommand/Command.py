import datetime
import socket
from time import sleep
from Sayer import say_message

morning_command_counter = 0


def Time_command():
    global morning_command_counter
    print("Time => " + str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(
        datetime.datetime.today().second) + "  |  Morning counter => " + str(morning_command_counter))

    try:
        if datetime.datetime.today().hour == 9 and datetime.datetime.today().minute == 0 and morning_command_counter == 0:
            sock = socket.socket()
            sock.connect(("localhost", 9090))
            sock.send('Morning'.encode("utf-8"))
            data = sock.recv(1024)
            sock.close()
            morning_command_counter = morning_command_counter + 1
            print(data.decode('utf-8'))
            sleep(6)
            say_message("Доброе утро сэр")
        elif datetime.datetime.today().hour == 22 and datetime.datetime.today().minute == 0 and morning_command_counter == 1:
            morning_command_counter = 0

    except:
        print(datetime.datetime.today().second)
    sleep(0.5)
