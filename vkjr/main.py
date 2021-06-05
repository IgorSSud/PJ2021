from Listener import *
from MainComand import *
from TimeComand import do_this_time_command

if __name__ == '__main__':
    while True:
        do_this_time_command()
        commmand = listen_command()
        do_this_command(commmand)
