# importing library
import sys, os, json, math
from time import perf_counter, sleep

# auto magic
try:
    from keyboard import is_pressed
except Exception:
    os.system("pip install keyboard")
    from keyboard import is_pressed

with open("settings.json", "r") as f:
    data = json.load(f)
    color = data["color"]
    resolution = data["resolution"]
    framerate = 1 / data["framerate"]
    movementSpeed = data["movementSpeed"]
    jumpTime = data["jumpTime"]
    fallTime = data["fallTime"]

jumpHeight = 4
scroll = 0
timePerFrame = 0.001

class player:
    size = 0
    jumpscore = 0
    onGround = False
    jumpStartHeight = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveLeft(self):
        pass

    def moveRight(self):
        pass

    def moveUp(self):
        pass

    def moveDown(self):
        pass

class game:
    def __init__(self, name):
        with open(f"maps/{name}", "r") as i:
            self.data = json.load(i)
            self.canvas = data["map"]
            self.pipes = data["pipe"]
            self.scrolls = data["scroll"]
            self.bgColor = data["bgColor"]

def gameLoop():
    keyListener()

def keyListener():
    if is_pressed("esc"):
        return True
    elif is_pressed("w") or is_pressed("up"):
        pass
    elif is_pressed("s") or is_pressed("down"):
        pass
    elif is_pressed("a") or is_pressed("left"):
        pass
    elif is_pressed("d") or is_pressed("right"):
        pass

    return False

gameLoop()
