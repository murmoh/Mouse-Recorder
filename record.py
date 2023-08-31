import time
from pynput.mouse import Controller
import win32api
import threading
import os

stop_event = threading.Event()


def start_recording():
    global stop_event
    stop_event.clear()
    t = threading.Thread(target=record)
    t.start()


def stop_recording():
    global stop_event
    stop_event.set()


def record():
    state_left = win32api.GetKeyState(0x01)
    state_right = win32api.GetKeyState(0x02)

    mouse = Controller()
    mousePos = mouse.position

    while not stop_event.is_set():
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)

        if a != state_left:
            state_left = a
            if a < 0:
                with open("mouseclickL.txt", "a+") as file1:
                    file1.writelines(str(mousePos) + "\n")

        if b != state_right:
            state_right = b
            if b < 0:
                with open("mouseclickR.txt", "a+") as file1:
                    file1.writelines(str(mousePos) + "\n")

        mousePos = mouse.position
        with open("mouse.txt", "a+") as file1:
            file1.writelines(str(mousePos) + "\n")

        time.sleep(0.1)

