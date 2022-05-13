# importing library
import os, json
from time import perf_counter, sleep

# auto magic
try:
    from keyboard import is_pressed
except Exception:
    os.system("pip install keyboard")
    from keyboard import is_pressed

try:
    from nilslib import clear, moveCursor, setTTYFgCol
except Exception:
    os.system("pip install keyboard")
    from nilslib import clear, moveCursor, setTTYFgCol

# load the settings from file
with open("settings.json", "r") as f:
    data = json.load(f)
    color = data["color"]
    resolution = data["resolution"]
    framerate = 1 / data["framerate"]
    movementSpeed = data["movementSpeed"]
    jumpTime = data["jumpTime"]
    fallTime = data["fallTime"]

# define some default values
jumpHeight = 4
scroll = 0 

# player class for the game as mario
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

# game class defines values for the level and saves the canvas
class game:
    def __init__(self, name):
        with open(f"maps/{name}.json", "r") as i:
            data = json.load(i)
            self.canvas = data["map"]
            self.pipes = data["pipe"]
            self.scrolls = data["scroll"]
            self.bgColor = data["bgColor"]

    def status(self):
        out = ""

        return out

    def draw(self):
        global scroll, color
        out = ""

        for y in range(resolution[1] - 1):
            x = scroll

            while x < resolution[0] + scroll:
                out += setTTYFgCol(color[self.canvas[y][x]][0], color[self.canvas[y][x]][1], color[self.canvas[y][x]][2])
                out += "██"

                while self.canvas[y][x] == self.canvas[y][x + 1] and x < ((resolution[0] -1) + scroll):
                    out += "██"
                    x += 1
                x += 1
            out += "\n"
        out += ("\x1b[0m")

        return out

# main loop
def gameLoop(level):
    moveCursor(resolution[1] + 2)

    isFinished = keyListener()
    output = ""

    output += level.status()
    output += level.draw()
    
    print(output)
    return isFinished

# listens for keys
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

# execute the game
level = game("1-1")

entities = {}
entities["mario"] = player(0, 0)

clear()
while True:
    if gameLoop(level):
        break
