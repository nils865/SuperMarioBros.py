import json

levelLength = 16 + 1

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
        data["map"][i].append("black")

# floor
for i in range(levelLength):
    data["map"][12].append("darkblue")
    data["map"][13].append("darkblue")

# wall
for i in range(12):
    data["map"][i][0] = "darkblue2"

# pipe
for i in range(12):
    data["map"][i][15] = "lightgreen"
data["map"][10][14] = "lightgreen"
data["map"][11][14] = "lightgreen"
data["map"][10][13] = "lightgreen"
data["map"][11][13] = "lightgreen"

# blocks
for i in range(7):
    for j in range(3):
        data["map"][j + 9][i + 4] = "darkblue2"

data["pipe"] = []
data["scroll"] = False
data["bgColor"] = "black"

data["pipe"].append([13, 10, "maps/1-1", "x", 163, 9, 157])
data["pipe"].append([13, 11, "maps/1-1", "x", 163, 9, 157])


print(len(data["map"]))
print(len(data["map"][0]))

with open("../map/1-1-sub.json", "w") as i :
   json.dump(data, i)