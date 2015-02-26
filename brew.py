#! /usr/local/bin/python3

import time
import datetime
import psutil
from subprocess import Popen


def toggle_cafe(seconds):
    for process in psutil.process_iter():
        if process.name() == 'afplay':
            print('Thank you for coming to Cafe Bastille.')
            process.terminate()
            break
    else:
        print('Timer set for {0} minute(s).'.format(seconds / 60))
        # Popen(args) system executuable, file, args -t == time '10' == seconds
        Popen(['afplay', 'sounds/sound0.mp3', '-t', str(seconds)])

def countdown(duration):
    time.sleep(duration/4)
    print("You're 1/4 of the way there.")
    time.sleep(duration/4)
    print("You're 1/2 of the way there.")
    time.sleep(duration/4)
    print("You're 3/4 of the way there.")
    time.sleep(duration/4)
    return

def brew():
  """
  Timer defaults to 4 minutes.
  Can be used for a longer/shorter timer if desired.
  """
  mins = input("How long to brew your coffee? ENTER for 4 minutes:\n> ")
  try:
    if mins == '':
      mins = 4
    else:
      mins = int(mins)
  except:
      mins = 4

  duration = mins * 60
  toggle_cafe(duration)
  countdown(duration)
  Popen(['afplay', 'sounds/times_up.mp3'])
  Popen(['say', 'Coffee is ready.'])

if __name__ == '__main__':
  brew()