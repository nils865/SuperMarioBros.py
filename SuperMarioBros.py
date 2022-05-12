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

class mario:
    size = 0
    jumpscore = 0
    onGround = False
    jumpStartHeight = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

player = mario(1, 1)

print(f"{player.x} {player.y} {player.size} {player.jumpscore} {player.jumpStartHeight} {player.onGround}")