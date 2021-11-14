
# Import modules

import os
import sys
import cv2
from tkinter import *

# Clear CMD

# Commands from sys.argv

count = 0
commands = {}
getType = ""
for argv in sys.argv:
    if ".py" not in argv.lower():
        if count == 0:
            getType = argv.replace("-", "")
            count += 1
        elif count == 1:
            commands[getType] = argv
            count = 0
    else:
        os.system("clear")
        print("\n{} {} (Python {})".format(argv.replace(".py", ""), cv2.__version__, sys.version.split(" ")[0]))

# Camera class

class Camera:

    def __init__(self, name=" "):
        self.name = name
        self.root = Tk()
        self.screen_size = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.camera = cv2.VideoCapture(0)
        self.write("DONE\nPreparing Screen ... ")
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.screen_size[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.screen_size[1])
        self.camera_size = (self.camera.get(3), self.camera.get(4))
        self.write("DONE\n\n")
        self.start()

    def write(self, text):
        self.text = text
        sys.stdout.flush()
        sys.stdout.write(self.text)

    def getCommand(self, type):
        self.type = type
        self.type = self.type.lower()
        try:
            self.response = commands[self.type]
        except:
            self.response = None
        return self.response

    def convert(self, frame):
        self.frame = frame
        self.frame = cv2.rotate(self.frame, cv2.ROTATE_180) # Rotate 180 Degrees
        return self.frame

    def start(self):
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while True:
            self.success, self.frame = self.camera.read()
            if self.success == False or cv2.waitKey(1) == ord(" "):
                break
            else:
                cv2.imshow(self.name, self.convert(self.frame))

# Initial run

if __name__ in "__main__":
    sys.stdout.flush()
    sys.stdout.write("\nCamera Initialising ... ")
    Camera()