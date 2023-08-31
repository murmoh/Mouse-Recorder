from tkinter import *
import record
import start
import logger


def erase_logs():
    erase.config(state=NORMAL)
    stop_button.config(state=DISABLED)


def erase_mouse():
    open('mouseclickL.txt', 'w').close()
    open('mouseclickR.txt', 'w').close()
    open('mouse.txt', 'w').close()


def on_record_click():
    record_button.config(state=DISABLED)
    stop_button.config(state=NORMAL)
    record.start_recording()


def on_stop_click():
    record_button.config(state=NORMAL)
    stop_button.config(state=DISABLED)
    record.stop_recording()


def on_start_click():
    speed = speed_slider.get()
    start.start(speed)


def on_log_click():
    logger.log()


root = Tk()
root.title("Mouse Recorder")

frame = Frame(root)
frame.pack(padx=10, pady=10)

record_button = Button(frame, text="Record", command=on_record_click)
record_button.grid(row=0, column=0, padx=5, pady=5)

stop_button = Button(frame, text="Stop", state=DISABLED, command=on_stop_click)
stop_button.grid(row=0, column=1, padx=5, pady=5)

start_button = Button(frame, text="Start", command=on_start_click)
start_button.grid(row=0, column=2, padx=5, pady=5)

log_button = Button(frame, text="Log", command=on_log_click)
log_button.grid(row=0, column=3, padx=5, pady=5)

speed_slider = Scale(frame, from_=10, to=200, orient=HORIZONTAL, label="Speed")
speed_slider.set(100)
speed_slider.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

erase = Button(frame, text="Erase Logs", command=erase_mouse)
erase.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()
