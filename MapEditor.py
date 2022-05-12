# importing library
from re import M
import sys, os, json, math
from time import perf_counter, sleep

# auto magic
try:
    from keyboard import is_pressed
except Exception:
    os.system("pip install keyboard")
    from keyboard import is_pressed

height = 14
name = input("Enter name: ")
width = int(input("Enter width: ")) + 1
bg = input("Enter Background color: ")

data = {}

data["maps"] = []

for i in range(height):
    data["maps"].append([])

data["bgColor"] = bg

for i in range(height):
    for j in range(width):
        data["maps"][i].append(bg)

with open(f"maps/{name}.json", "w") as f:
    json.dump(data, f)