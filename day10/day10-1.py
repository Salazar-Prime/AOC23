##### BEGIN BOIER CODE #####
import sys, os, re
import numpy as np
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 10
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####
dataCopy = data.copy()

#### MAPPPING ####
# fmt: off
symbolMap = { "|": (1,0,1,0), "-": (0,1,0,1), "L": (1,1,0,0), "7": (0,0,1,1), "J": (1,0,0,1), "F": (0,1,1,0), "Z": (1,1,1,1)  }
gotoPos ={"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
nextDirMap = {"N": "S", "S": "N", "E": "W", "W": "E"}
directions = ["N", "E", "S", "W"]
# fmt: on

#### CODE ####
# find "S"
for y, line in enumerate(data):
    if "S" in line:
        x = line.index("S")
        # replace S with "Z"
        data[y] = line[:x] + "Z" + line[x + 1 :]
        break
# found "S"
pos = (x, y)

# find the start direction and enter NN
for dir in directions:
    nd = nextDirMap[dir]
    #  elementwise
    newPos = addT(pos, gotoPos[nd], dataCopy)
    if checkDir(newPos, nd, symbolMap, directions, data):
        pos = newPos
        nd = getNextNode(pos, nd)
        break

count = 0
# start walking
while True:
    symbol = data[pos[1]][pos[0]]
    if symbol == "Z":
        break
    count += 1

    pos = addT(pos, gotoPos[nd], dataCopy)
    nd = getNextNode(pos, nextDirMap[nd], symbolMap, directions, data)

print(count)
