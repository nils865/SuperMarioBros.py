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
name = "test" # input("Enter name: ")
width = 20 # int(input("Enter width: ")) + 1
bg = "w" # input("Enter Background color: ")
scrolls = True # bool(input("Enter if level scrolls: "))

data = {}

data["maps"] = []

for i in range(height):
    data["maps"].append([])

data["bgColor"] = bg

for i in range(height):
    for j in range(width):
        data["maps"][i].append(bg)

game = data["maps"]
scroll = 0
with open("settings.json", "r") as f:
    data = json.load(f)
    framerate = 1 / data["framerate"]
    color = data["color"]

def setcolor(r,g,b):
    return(f"\x1b[38;2;{r};{g};{b}m")

if os.name == 'nt':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')

def draw():
    global game, color, scroll, scrolls
    out = ""

    for i in range(height - 1):
        j = 0
        if scrolls:
            j = scroll
        while j < ((width - 2) + scroll):
            out += setcolor(color[game[i][j]][0], color[game[i][j]][1], color[game[i][j]][2])
            out += ("██")
            while game[i][j] == game[i][j + 1] and j < width:
                out += ("██")  
                j += 1
            j += 1
        out += ("\n")
    out += ("\x1b[0m")  

    return out

def goUp(lines):
   sys.stdout.write("\x1b[1A" * lines) 

def keyListener():
    if is_pressed('esc'):
        return True
    elif is_pressed('w'):
        pass
    elif is_pressed('a'):
        pass
    elif is_pressed('s'):
        pass
    elif is_pressed('d'):
        pass
    return False

clear()
while True:
    t = perf_counter()
    goUp((height))
    
    if keyListener():
        break

    print(draw())

    if (perf_counter() - t) < framerate:
        sleep(framerate - (perf_counter() - t))

with open(f"maps/{name}.json", "w") as f:
    json.dump(data, f)