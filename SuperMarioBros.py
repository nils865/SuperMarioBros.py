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