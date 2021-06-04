from Listener import *
from MainComand import *


if __name__ == '__main__':
  while True:
      commmand=listen_command()
      do_this_command(commmand)

