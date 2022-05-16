from nilslib import setTTYFgCol, resetColor

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (128, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 128, 255),
    (0, 0, 255),
    (128, 0, 255),
    (255, 0, 255),
    (255, 128, 255),
    (255, 255, 255),
    (128, 128, 128),
    (64, 255, 64),
    (255, 64, 64),
]

colors2 = [
    (255, 64, 64),
    (0, 0, 0),
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (128, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 128, 255),
    (0, 0, 255),
    (128, 0, 255),
    (255, 0, 255),
    (255, 128, 255),
    (255, 255, 255),
    (128, 128, 128),
    (64, 255, 64),
]

def draw():
    out = ""

    for i in range(64):

        k = 0
        c = 0

        for l in range(16):
            for j in range(128):
                if k >= 16:
                    out += setTTYFgCol(colors[c][0], colors[c][1], colors[c][2])
                    k = 0
                    c += 1
                    pass
                k += 1
                out += ("██")
            k = 0
        
        k = 0
        out += "\n"

        for l in range(16):
            for j in range(128):
                if k >= 16:
                    out += setTTYFgCol(colors2[c][0], colors2[c][1], colors2[c][2])
                    k = 0
                    c += 1
                    pass
                k += 1
                out += ("██")
            k = 0
        
        k = 0
        out += "\n"
    
    return str(out)


print(draw())
resetColor()
