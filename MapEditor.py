# importing library
import sys, os, json, math
from time import perf_counter, sleep

# auto magic
try:
    from keyboard import is_pressed
except Exception:
    os.system("pip install keyboard")
    from keyboard import is_pressed

height = 14
width = int(input("Enter width: ")) + 1
bg = input("Enter Background color: ")