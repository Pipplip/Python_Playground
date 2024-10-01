import pyautogui
import math
import ctypes
import threading
import time
import sys
import random
from pynput import keyboard

""" Mouse mouse Thread class """
class MouseMoveThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self) # Oberklasse von Thread aufrufen
        self.id = id
        self.name = name

    def run(self):
        print("Starte MouseMoveThread ", self.id)
        #self.circle()
        self.random_movement()

    def get_screen_center(self):
        user32 = ctypes.windll.user32
        screencenter = user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2
        return screencenter

    def circle(self):
        #a,b = pyautogui.position()
        a,b = self.get_screen_center()
        w = 20
        m = (2*math.pi)/w

        r = 200      

        global stop_app

        while 1:
            for i in range(w+1):
                if stop_app == False:
                    x = int(a+r*math.sin(m*i))  
                    y = int(b+r*math.cos(m*i))
                    pyautogui.moveTo(x, y, duration = 0.2)
                else:
                    sys.exit()
                    break

    def random_movement(self):
        #a,b = pyautogui.position()
        a,b = self.get_screen_center()
        r = 200      

        global stop_app

        while 1:
            
            if stop_app == False:
                x = random.randint(1,r) + a
                y = random.randint(1,r) + b
                pyautogui.moveTo(x, y, duration = 0.05)
            else:
                sys.exit()
                break
            



""" Key Event Thread class """
class KeyEventThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self) # Oberklasse von Thread aufrufen
        self.id = id
        self.name = name

    def run(self):
        print("Starte KeyEventThread ", self.id)
        self.init_listener()

    def init_listener(self):
        listener = keyboard.Listener(on_press=self.on_key_press)
        listener.start()  # start to listen on a separate thread
        listener.join()  # remove if main thread is polling self.keys

    def on_key_press(self, key):
        global stop_app

        if key == keyboard.Key.esc or key == keyboard.Key.enter:
            print('Key pressed: ' , str(key))
            stop_app = True
            print("Vor sys.exit")
            sys.exit()
            print("Nach sys.exit")
            return False  # stop listener
#        try:
#            k = key.char  # single-char keys
#        except:
#            k = key.name  # other keys
#        if k in ['1', '2', 'left', 'right']:  # keys of interest
#            # self.keys.append(k)  # store it in global-like variable
#            print('Key pressed: ' + k)
#            stop_app = True
#            return False  # stop listener; remove this if want more keys


if __name__ == "__main__":

    stop_app = False
    threads_running = True

    try:
        t1 = KeyEventThread(1,"KeyEventThread")
        t2 = MouseMoveThread(2,"MouseMoveThread")
        t1.start()
        time.sleep(0.5)
        t2.start()

        while threads_running:
            if t1.is_alive() == False and t2.is_alive() == False:
                print("Beide Threads sind fertig. Exit application!")
                threads_running = False


    except KeyboardInterrupt as e:   
        print("App closed")

    except:
        print("Exception")


#    try:
#        #circle()
#        listener = keyboard.Listener(on_press=on_key_press)
#        listener.start()  # start to listen on a separate thread
#        listener.join()  # remove if main thread is polling self.keys
#    except KeyboardInterrupt as e:
#       print("Keep up the good work... ;-)")
