import logging
import threading
import time

import requests

import huebulb as hue

livingRoom = hue.Bulb(id=1)
bedroom = hue.Bulb(id=2)

def thread1(name):
    global thread1_complete
    thread1_complete = False
    livingRoom.set_value(254)
    livingRoom.rainbow(cycles=1, speed=11000)
    livingRoom.set_value(0)
    livingRoom.show()
    thread1_complete = True


def thread2(name):
    bedroom.set_value(254)
    bedroom.rainbow(cycles=20, speed=180)

x = threading.Thread(target=thread1, args=(0,), daemon=True, name='thread1')
x.start()

y = threading.Thread(target=thread2, args=(1,), daemon=True, name='thread2')
y.start()

while(True):
    # x.join()
    if (thread1_complete):
        print("Terminating Thread 1...")
        thread1_complete = False
        x.join()

    if(x.is_alive == False):
        print('thread1 is dead, restarting...')
        x.start
    else:
        print('thread1 is alive')
    time.sleep(2)
