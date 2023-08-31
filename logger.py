import subprocess
from tkinter import *
from tkinter import messagebox
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import psutil

# Get the default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


def log():
    def set_app_volume(value, session):
        volume_control = session.SimpleAudioVolume
        volume_control.SetMasterVolume(value / 100, None)

    def get_active_sessions():
        sessions = []
        for session in AudioUtilities.GetAllSessions():
            if session.Process:
                try:
                    process = psutil.Process(session.Process.pid)
                    process_name = process.name()
                    if process and process_name and process_name not in [session[0] for session in sessions]:
                        sessions.append((process_name, session))
                except psutil.NoSuchProcess:
                    pass
        return sessions

    def end_task():
        selected_app = listbox.selection_get()
        for process in psutil.process_iter(["name", "pid"]):
            if process.info["name"] == selected_app:
                try:
                    process.terminate()
                    messagebox.showinfo("Task Ended", f"The task {selected_app} has been terminated.")
                    update_listbox()
                    break
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to terminate the task {selected_app}: {str(e)}")
                    break

    def update_listbox():
        sessions = get_active_sessions()
        for i in range(len(sessions)):
            title, session = sessions[i]
            listbox.delete(i, END)
            listbox.insert(i, title)

            app_volume = int(session.SimpleAudioVolume.GetMasterVolume() * 100)
            scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL,
                          command=lambda value, s=session: set_app_volume(float(value), s))
            scale.grid(row=i, column=1, padx=(5, 0))
            scale.set(app_volume)

    log_window = Toplevel()
    log_window.title("Active Windows")

    frame = Frame(log_window)
    frame.pack(padx=10, pady=10)

    listbox = Listbox(frame, width=40, height=20)
    listbox.grid(row=0, column=0, padx=5, pady=5, rowspan=len(get_active_sessions()))

    # Add volume sliders in a separate column
    for i in range(len(get_active_sessions())):
        app_volume = int(get_active_sessions()[i][1].SimpleAudioVolume.GetMasterVolume() * 100)
        scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL,
                      command=lambda value, s=get_active_sessions()[i][1]: set_app_volume(float(value), s))
        scale.grid(row=i, column=1, padx=(5, 0))
        scale.set(app_volume)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
    scrollbar.grid(row=0, column=2, sticky="ns", pady=5, rowspan=len(get_active_sessions()))
    listbox.config(yscrollcommand=scrollbar.set)

    refresh_button = Button(frame, text="Refresh", command=update_listbox)
    refresh_button.grid(row=len(get_active_sessions()), column=0, padx=5, pady=5)

    end_task_button = Button(frame, text="End Task", command=end_task)
    end_task_button.grid(row=len(get_active_sessions()), column=1, padx=5, pady=5)

    update_listbox()


def logi():
    import os, sys
    import subprocess

    run = False
    if not run:
        run2 = True
    run2 = True

    # run2 deletes previous files
    while run2:
        open("app", "w+")
        os.remove("app.txt")
        open("app.txt", "w+")
        run = True
        run2 = False
    while run:
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if line.rstrip():
                # only print lines that are not empty
                # decode() is necessary to get rid of the binary string (b')
                # rstrip() to remove `\r\n`
                print(line.decode(errors='ignore').rstrip())
                file1 = open("app.txt", "a+")
                file1.writelines(str(line.decode(errors='ignore').rstrip()) + "\n")
                run = False

if __name__ == "__main__":
    root = Tk()
    root.title("Volume Controller")
    root.geometry("800x400")

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu)
    main_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Log Active Windows", command=log)

    root.mainloop()
    logi()
