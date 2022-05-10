import sys, os, json, math
from time import perf_counter, sleep
try:
    from keyboard import is_pressed
except Exception:
    os.system("pip install keyboard")
    from keyboard import is_pressed

resolution = (16, 15)
framerate = 1 / 35
startTime = perf_counter()
color = {
    "black": (0, 0, 0),
    "red": (252, 32, 0),
    "orange": (255, 128, 0),
    "yellow": (251, 152, 56),
    "lightgreen": (128, 208, 16),
    "lightblue": (93, 148, 251),
    "brown": (200, 76, 12),
    "brown2": (210, 76, 12),
    "brown3": (190, 76, 12),
    "darkgreen": (0, 168, 0),
    "white": (255, 255, 255),
    "darkblue": (0, 84, 122),
    "darkblue2": (0, 88, 123),
    "coin": (184, 131, 47)
}
with open("maps/1-1.json", "r") as i:
    data = json.load(i)
    game = data["map"]
    pipes = data["pipe"]
    scrolls = data["scroll"]
    bgColor = data["bgColor"]
scroll = 0
status = ""
movementSpeed = 15
jumpHeight = 4
jumpTime = 13
fallTime = 13
timePerFrame = 0.001
mario = {
    "x": 0,
    "y": 0,
    "size": 0,
    "jumpscore": 0,
    "onGround": False,
    "jumpStartHeight": 0,
}

if os.name == 'nt':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')

def setcolor(r,g,b):
    return(f"\x1b[38;2;{r};{g};{b}m")

def draw():
    global game, color, scroll, scrolls
    out = ""
    
    out += status + " " * 20 + "\n"
    for i in range(resolution[1] - 1):
        j = 0
        if scrolls:
            j = scroll
        while j < ((resolution[0]) + scroll):
            out += setcolor(color[game[i][j]][0], color[game[i][j]][1], color[game[i][j]][2])
            out += ("██")
            while game[i][j] == game[i][j + 1] and (j < ((resolution[0] - 1) + scroll)):
                out += ("██")  
                j += 1
            j += 1
        out += ("\n")
    out += ("\x1b[0m")  

    return out

def keyListener():
    global mario, pipes
    if is_pressed('esc'):
        return True
    elif is_pressed('w') and mario["jumpscore"] == 0 and mario["onGround"]:
        jump()
    elif is_pressed('a') and not mario["x"] < (scroll + 1):
        return colisionDetection("left")
    elif is_pressed('s'):
        for i in pipes:
            if int(mario["x"]) == i[0] and int(mario["y"]) == (i[1] - 1) and i[3] == "y" and mario["onGround"]:
                warp(i[2], i[4], i[5], i[6])
    elif is_pressed('d'):
        for i in pipes:
            if int(mario["x"]) == (i[0] - 1) and int(mario["y"]) == i[1] and i[3] == "x" and mario["onGround"]:
                warp(i[2], i[4], i[5], i[6])
        colisionDetection("right")
    return False

def drawMario():
    game[int(mario["y"])][int(mario["x"])] = "red"

def clampto(comma, number):
    return int(number * (10 ** comma)) / (10 ** comma)

def spawnMario():
    mario["x"] = 3
    mario["y"] = 11

def jump():
    global mario
    mario["jumpStartHeight"] = mario["y"]
    mario["jumpscore"] = jumpHeight
    
def fallDetection():
    global mario, game, bgColor, fallTime, timePerFrame
    if mario["jumpscore"] == 0 and game[int(mario["y"]) + 1][int(mario["x"])] == bgColor and not int(mario["y"] + 1) > resolution[1]:
        mario["y"] += fallTime * timePerFrame
        mario["onGround"] = False
    else:
        mario["onGround"] = True

def colisionDetection(direction):
    global game, mario, bgColor
    if int(mario["x"] - movementSpeed * timePerFrame) < 0:
            return True

    if direction == "left" and game[int(mario["y"])][int((mario["x"] - movementSpeed * timePerFrame))] == bgColor:
        mario["x"] -= movementSpeed * timePerFrame
    elif direction == "right" and game[int(mario["y"])][int(mario["x"] + movementSpeed * timePerFrame)] == bgColor:
        mario["x"] += movementSpeed * timePerFrame

def warp(zone, x, y, newScroll):
    global game, pipes, scrolls, scroll, bgColor
    scroll = newScroll
    mario["x"] = x
    mario["y"] = y
    with open(f"{zone}.json", "r") as i:
        data = json.load(i)
        game = data["map"]
        pipes = data["pipe"]
        scrolls = data["scroll"]
        bgColor = data["bgColor"]

clear()
spawnMario()
while True:
    t = perf_counter()
    sys.stdout.write("\x1b[1A" * (resolution[1] + 2))

    game[int(mario["y"])][int(mario["x"])] = bgColor
    if keyListener() or mario["x"] < (scroll) or mario["x"] > (len(game[0]) - 1) or mario["x"] > (len(game[0]) - 1) or int(mario["y"]) > resolution[1] - 3:
        clear()
        print(f"Game Over")
        break
    elif game[int(mario["y"])][int(mario["x"] + 1)] == "darkgreen":
        clear()
        print(f"You Win!\nTime: {clampto(2, perf_counter() - startTime)}")
        break
    
    if mario["jumpscore"] > 0:
        if mario["jumpStartHeight"] - jumpHeight > (mario["y"] - (jumpTime * timePerFrame)):
            mario["jumpscore"] = 0
        elif not game[int(mario["y"] - jumpTime * timePerFrame )][int(mario["x"])] == bgColor:
            mario["jumpscore"] = 0
        else:
            mario["jumpscore"] -= jumpTime * timePerFrame
            mario["y"] -= jumpTime * timePerFrame 
    else:
        mario["jumpscore"] = 0

    if mario["x"] > ((resolution[0] + scroll) - 8) and not (resolution[0] + scroll) > (len(game[0]) - 1) and scrolls:
        scroll += 1 

    fallDetection()
    drawMario()

    status += f" | Scroll: {scroll} | Time: {clampto(2, perf_counter() - startTime)}\nX: {int(mario['x'])} | Y: {int(mario['y'])} | Jumpscore: {int(mario['jumpscore'])} | OnGround: {mario['onGround']} | Scroll: {scroll}"

    print(draw())

    status = ""

    if (perf_counter() - t) < framerate:
        sleep(framerate - (perf_counter() - t))
    timePerFrame = (perf_counter() - t)
    status += "FPS: " + str(int(1 / (timePerFrame)))
    status.replace("e", "")

