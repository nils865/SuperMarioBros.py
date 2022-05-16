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

def draw():
    out = ""

    for i in range(255):

        k = 0
        c = 0

        for j in range(255):
            if k >= 16:
                out += setTTYFgCol(colors[c][0], colors[c][1], colors[c][2])
                k = 0
                c += 1
                pass
            k += 1
            out += ("██")
        
        k = 0
        out += "\n"
    
    return out


print(colors[1])
print(draw())
resetColor()