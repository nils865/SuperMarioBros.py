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
bg = "lb" # input("Enter Background color: ")
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
    settings = json.load(f)
    framerate = 1 / settings["framerate"]
    resolution = settings["resolution"]
    color = settings["color"]

def setcolor(r,g,b):
    return(f"\x1b[38;2;{r};{g};{b}m")

if os.name == 'nt':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')

class cursor:
    x = 0
    y = 0
    currentColor = bg

    def draw(self):
        self.currentColor = game[self.y][self.x]
        game[self.y][self.x] = "w"

    def scroll(self):
        global scroll, resolution
        if self.x > ((resolution[0] + scroll) - 8) and not (resolution[0] + scroll) > (len(game[0]) - 1) and scrolls:
            scroll += 1 

def draw():
    global game, color, scroll, scrolls, resolution
    out = ""

    for i in range(resolution[1] - 1):
        j = 0
        if scrolls:
            j = scroll
        while j < ((resolution[0]) + scroll):
            out += setcolor(color[game[i][j]][0], color[game[i][j]][1], color[game[i][j]][2])
            out += ("██")
            try:
                while game[i][j] == game[i][j + 1] and (j < ((resolution[0] - 1) + scroll)):
                    out += ("██")
                    j += 1
            except Exception:
                pass
            j += 1
        out += ("\n")
    out += ("\x1b[0m")  

    return out

def goUp(lines):
   sys.stdout.write("\x1b[1A" * lines) 

def keyListener(cursor):
    if is_pressed('esc'):
        clear()
        return True
    elif is_pressed('w') and not (cursor.y - 1) < 0:
        cursor.y -= 1
        pass
    elif is_pressed('a') and not (cursor.x - 1) < 0:
        cursor.x -= 1
        pass
    elif is_pressed('s') and not (cursor.y + 1) > (height - 1):
        cursor.y += 1
        pass
    elif is_pressed('d') and not (cursor.x + 1) > (width - 1):
        cursor.x += 1
        pass
    return False

cursor1 = cursor()
status = ""
clear()
while True:
    t = perf_counter()
    goUp((resolution[0] + 1))

    status += f"X: {cursor1.x} Y: {cursor1.y} Color: {cursor1.currentColor}                "
    
    game[cursor1.y][cursor1.x] = cursor1.currentColor
    
    if keyListener(cursor1):
        break

    cursor1.scroll()

    cursor1.draw()
    
    print(status)
    print(draw())
    
    status = ""

    if (perf_counter() - t) < framerate:
        sleep(framerate - (perf_counter() - t))

with open(f"maps/{name}.json", "w") as f:
    json.dump(data, f)
