import time
from pynput.mouse import Button, Controller

def start(speed):
    mouse = Controller()

    with open("mouse.txt", "r") as f:
        lines = f.readlines()

    with open("mouseclickL.txt", "r") as f:
        left_clicks = [line.strip().strip("()").split(",") for line in f.readlines()]

    with open("mouseclickR.txt", "r") as f:
        right_clicks = [line.strip().strip("()").split(",") for line in f.readlines()]

    for line in lines:
        x, y = line.strip().strip("()").split(",")

        mouse.position = (float(x), float(y))

        if [x, y] in left_clicks:
            mouse.click(Button.left, 1)
        elif [x, y] in right_clicks:
            mouse.click(Button.right, 1)

        time.sleep(1.0 / speed)
