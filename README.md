# Mouse Recorder and Manager
This repository hosts a utility built using Python and tkinter that provides functionalities related to mouse activities and application management.

## Features:
Mouse Movement and Click Recorder: Record real-time mouse movements and clicks, saving the data to corresponding files (mouse.txt, mouseclickL.txt, mouseclickR.txt).

Mouse Playback: Play the recorded mouse movements and clicks with an adjustable speed control.

Log Active Windows and Control Volume:

List all the active windows on the system.
Adjust the volume of applications individually.
Terminate a selected active task.
Refresh the list of active windows.
Log Applications: Logs the description of applications with active main windows to an app.txt file.

Erase Logs: Delete the recorded mouse activity logs from their respective files.

## Components:
1. Main UI (tkinter GUI):
Buttons for recording, stopping the recording, starting the playback, logging active windows, and erasing logs.
Speed control slider for playback.
2. Mouse Playback:
Reads the recorded data and replicates the mouse movements and clicks with the given speed.
3. Active Windows Logger:
Uses the psutil and pycaw.pycaw libraries to fetch and display the list of active windows.
Provides volume control for each application.
Enables users to end tasks directly from the GUI.
4. Mouse Recording:
Uses pynput and win32api to record mouse movements and clicks in real-time.
Writes this data to dedicated files.
Installation:
You need to install the required packages. The main dependencies include tkinter, pynput, pycaw, psutil, and win32api.

Copy code
pip install pynput psutil pycaw pywin32
How to Run:
Copy code
python main_script_name.py
Replace main_script_name.py with the name of your main script if it's not as stated.
