##### BEGIN BOIER CODE #####
import sys, os, re
import numpy as np

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


def addT(t1, t2, dataCopy=dataCopy):
    tp = tuple(map(sum, zip(t1, t2)))
    # replace chacrter in dataCopy at tp with "O"
    dataCopy[tp[1]] = dataCopy[tp[1]][: tp[0]] + "O" + dataCopy[tp[1]][tp[0] + 1 :]
    # replace symvols oin dataCopy following zip
    # zip("|JL7F-", "│┘└┐┌─")
    translation_table = str.maketrans("|JL7F-", "│┘└┐┌─")
    # apply tranlastion table
    dataCopy = [line.translate(translation_table) for line in dataCopy]

    # replace with unicode mapping
    # save it to newMap.txt
    with open("newMap.txt", "w") as f:
        f.write("".join(dataCopy))
    return tp


def checkDir(pos, dir):
    symbolNodes = symbolMap[data[pos[1]][pos[0]]]
    checkSubNode = directions.index(dir)
    if symbolNodes[checkSubNode] == 1:
        return True
    return False


def getNextNode(pos, entryDir):
    x, y = pos
    # get symbol nodes
    symbol = data[y][x]
    symbolNodes = symbolMap[data[y][x]]
    # get index of all ones
    ones = [i for i, x in enumerate(symbolNodes) if x == 1]
    ones.remove(directions.index(entryDir))
    # remove index directions[entryDir]
    return directions[ones[0]]


#### CODING ####

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
    if checkDir(newPos, nd):
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
    nd = getNextNode(pos, nextDirMap[nd])

print(count)
