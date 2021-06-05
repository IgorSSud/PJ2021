import datetime
import socket
from time import sleep
from Sayer import say_message


def do_this_time_command():
    print(datetime.datetime.today().second)
    if datetime.datetime.today().second == 30:
    #elif "доброе утро" in message:
        sock = socket.socket()
        sock.connect(("localhost", 9090))
        sock.send('hello!'.encode("utf-8"))
        data = sock.recv(1024)
        sock.close()
        print(data.decode('utf-8'))
        sleep(4)
        say_message("Доброе утро сэр")