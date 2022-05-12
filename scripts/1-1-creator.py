import json

levelLength = 212 + 1

data = {
    "map": [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ],
}

# sky
for i in range(len(data["map"]) - 2):
    for j in range(levelLength):
        data["map"][i].append("lightblue")

# floor
for j in range(levelLength):
    data["map"][12].append("brown")
    data["map"][13].append("brown")

# pipe 1
data["map"][11][28] = "lightgreen"
data["map"][11][29] = "lightgreen"
data["map"][10][28] = "lightgreen"
data["map"][10][29] = "lightgreen"

# pipe 2
data["map"][11][39] = "lightgreen"
data["map"][11][38] = "lightgreen"
data["map"][10][38] = "lightgreen"
data["map"][10][39] = "lightgreen"
data["map"][9][38] = "lightgreen"
data["map"][9][39] = "lightgreen"

# pipe 3
data["map"][11][46] = "lightgreen"
data["map"][11][47] = "lightgreen"
data["map"][10][46] = "lightgreen"
data["map"][10][47] = "lightgreen"
data["map"][9][46] = "lightgreen"
data["map"][9][47] = "lightgreen"
data["map"][8][46] = "lightgreen"
data["map"][8][47] = "lightgreen"

# pipe 4
data["map"][11][57] = "lightgreen"
data["map"][11][58] = "lightgreen"
data["map"][10][57] = "lightgreen"
data["map"][10][58] = "lightgreen"
data["map"][9][57] = "lightgreen"
data["map"][9][58] = "lightgreen"
data["map"][8][57] = "lightgreen"
data["map"][8][58] = "lightgreen"

# pipe 5
data["map"][11][163] = "lightgreen"
data["map"][11][164] = "lightgreen"
data["map"][10][163] = "lightgreen"
data["map"][10][164] = "lightgreen"

# pipe 6
data["map"][11][179] = "lightgreen"
data["map"][11][180] = "lightgreen"
data["map"][10][179] = "lightgreen"
data["map"][10][180] = "lightgreen"

# hole 1
data["map"][12][69] = "lightblue"
data["map"][12][70] = "lightblue"
data["map"][13][69] = "lightblue"
data["map"][13][70] = "lightblue"

# hole 2
data["map"][12][86] = "lightblue"
data["map"][12][87] = "lightblue"
data["map"][12][88] = "lightblue"
data["map"][13][86] = "lightblue"
data["map"][13][87] = "lightblue"
data["map"][13][88] = "lightblue"

# hole 3
data["map"][12][153] = "lightblue"
data["map"][12][154] = "lightblue"
data["map"][13][153] = "lightblue"
data["map"][13][154] = "lightblue"

# blocks 1
data["map"][8][16] = "yellow"

data["map"][8][20] = "brown2"
data["map"][8][21] = "yellow"
data["map"][8][22] = "brown2"
data["map"][4][22] = "yellow"
data["map"][8][23] = "yellow"
data["map"][8][24] = "brown2"

# blocks 2
data["map"][8][77] = "brown2"
data["map"][8][78] = "yellow"
data["map"][8][79] = "brown2"

data["map"][4][80] = "brown2"
data["map"][4][81] = "brown2"
data["map"][4][82] = "brown2"
data["map"][4][83] = "brown2"
data["map"][4][84] = "brown2"
data["map"][4][85] = "brown2"
data["map"][4][86] = "brown2"
data["map"][4][87] = "brown2"

data["map"][4][91] = "brown2"
data["map"][4][92] = "brown2"
data["map"][4][93] = "brown2"
data["map"][4][94] = "yellow"
data["map"][8][94] = "brown2"
data["map"][8][100] = "brown2"

# blocks 3
data["map"][8][106] = "yellow"
data["map"][8][109] = "yellow"
data["map"][4][109] = "yellow"
data["map"][8][112] = "yellow"

# blocks 4
data["map"][8][118] = "brown2"

data["map"][4][121] = "brown2"
data["map"][4][122] = "brown2"
data["map"][4][123] = "brown2"

data["map"][4][128] = "brown2"
data["map"][4][129] = "yellow"
data["map"][4][130] = "yellow"
data["map"][4][131] = "brown2"

data["map"][8][129] = "brown2"
data["map"][8][130] = "brown2"

# blocks 5
data["map"][8][168] = "brown2"
data["map"][8][169] = "brown2"
data["map"][8][170] = "yellow"
data["map"][8][171] = "brown2"

# staircase 1
data["map"][11][134] = "brown3"
data["map"][11][135] = "brown3"
data["map"][11][136] = "brown3"
data["map"][11][137] = "brown3"

data["map"][10][135] = "brown3"
data["map"][10][136] = "brown3"
data["map"][10][137] = "brown3"

data["map"][9][136] = "brown3"
data["map"][9][137] = "brown3"

data["map"][8][137] = "brown3"

# staircase 2
data["map"][11][143] = "brown3"
data["map"][11][142] = "brown3"
data["map"][11][141] = "brown3"
data["map"][11][140] = "brown3"

data["map"][10][142] = "brown3"
data["map"][10][141] = "brown3"
data["map"][10][140] = "brown3"

data["map"][9][141] = "brown3"
data["map"][9][140] = "brown3"

data["map"][8][140] = "brown3"

# staircase 3
data["map"][11][148] = "brown3"
data["map"][11][149] = "brown3"
data["map"][11][150] = "brown3"
data["map"][11][151] = "brown3"
data["map"][11][152] = "brown3"

data["map"][10][149] = "brown3"
data["map"][10][150] = "brown3"
data["map"][10][151] = "brown3"
data["map"][10][152] = "brown3"

data["map"][9][150] = "brown3"
data["map"][9][151] = "brown3"
data["map"][9][152] = "brown3"

data["map"][8][151] = "brown3"
data["map"][8][152] = "brown3"

# staircase 4
data["map"][11][158] = "brown3"
data["map"][11][157] = "brown3"
data["map"][11][156] = "brown3"
data["map"][11][155] = "brown3"

data["map"][10][157] = "brown3"
data["map"][10][156] = "brown3"
data["map"][10][155] = "brown3"

data["map"][9][156] = "brown3"
data["map"][9][155] = "brown3"

data["map"][8][155] = "brown3"

# staircase 5
data["map"][11][181] = "brown3"
data["map"][11][182] = "brown3"
data["map"][11][183] = "brown3"
data["map"][11][184] = "brown3"
data["map"][11][185] = "brown3"
data["map"][11][186] = "brown3"
data["map"][11][187] = "brown3"
data["map"][11][188] = "brown3"
data["map"][11][189] = "brown3"

data["map"][10][182] = "brown3"
data["map"][10][183] = "brown3"
data["map"][10][184] = "brown3"
data["map"][10][185] = "brown3"
data["map"][10][186] = "brown3"
data["map"][10][187] = "brown3"
data["map"][10][188] = "brown3"
data["map"][10][189] = "brown3"

data["map"][9][183] = "brown3"
data["map"][9][184] = "brown3"
data["map"][9][185] = "brown3"
data["map"][9][186] = "brown3"
data["map"][9][187] = "brown3"
data["map"][9][188] = "brown3"
data["map"][9][189] = "brown3"

data["map"][8][184] = "brown3"
data["map"][8][185] = "brown3"
data["map"][8][186] = "brown3"
data["map"][8][187] = "brown3"
data["map"][8][188] = "brown3"
data["map"][8][189] = "brown3"

data["map"][7][185] = "brown3"
data["map"][7][186] = "brown3"
data["map"][7][187] = "brown3"
data["map"][7][188] = "brown3"
data["map"][7][189] = "brown3"

data["map"][6][186] = "brown3"
data["map"][6][187] = "brown3"
data["map"][6][188] = "brown3"
data["map"][6][189] = "brown3"

data["map"][5][187] = "brown3"
data["map"][5][188] = "brown3"
data["map"][5][189] = "brown3"

data["map"][4][188] = "brown3"

data["map"][4][189] = "brown3"

# flag
data["map"][11][198] = "brown3"
data["map"][10][198] = "darkgreen"
data["map"][9][198] = "darkgreen"
data["map"][8][198] = "darkgreen"
data["map"][7][198] = "darkgreen"
data["map"][6][198] = "darkgreen"
data["map"][5][198] = "darkgreen"
data["map"][4][198] = "darkgreen"
data["map"][3][198] = "darkgreen"
data["map"][2][198] = "darkgreen"
data["map"][1][198] = "white"

data["pipe"] = []

data["pipe"].append([57, 8, "maps/1-1-sub", "y", 3, 2, 0])
data["pipe"].append([58, 8, "maps/1-1-sub", "y", 3, 2, 0])  

data["scroll"] = True

data["bgColor"] = "lightblue"

print(len(data["map"]))
print(len(data["map"][0]))

with open("./maps/1-1.json", "w") as i :
   json.dump(data, i)