##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *
import functools

sys.setrecursionlimit(20000)

sys.path.insert(1, "common")
from utils import *

test = False
currentDay = 16
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####
grid = convertToNumpyArrayStr(data)
gridView = grid.copy()
# -----> X
# |
# |
# |
# ⌄
# Y

directions = ["U", "R", "D", "L"]
target = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
nextDirection = {
    "temp": ("/", "\\", "|", "-"),
    "L": ("D", "U", "UD", "L"),
    "D": ("L", "R", "D", "LR"),
    "R": ("U", "D", "UD", "R"),
    "U": ("R", "L", "U", "LR"),
}
energizedCoordinates = set()


def updateGrid(src):
    if not getChar(src) in nextDirection["temp"]:
        gridView[src[1]][src[0]] = "#"
    # convert each row to string
    gridViewList = ["".join(row) for row in gridView]
    saveToFile(gridViewList, f"day{currentDay}/gridView.txt")


def getChar(src):
    return grid[src[1]][src[0]]


def outOfBounds(direction, src):
    # returns 1 if beam is outside the bounds else 0
    if src[0] < 0 or src[0] >= len(grid[0]) or src[1] < 0 or src[1] >= len(grid):
        return 1
    if test:
        updateGrid(src)
    # create a tuple of the current src and direction
    energizedCoordinates.add((src, direction))


# @functools.cache
def beamMove(direction, src):
    # move beam. Get target
    dest = addT(src, target[direction])
    if (dest, direction) in energizedCoordinates:
        return 1
    if outOfBounds(direction, dest):
        return 1
    destChar = getChar(dest)

    match destChar:
        case ".":
            beamMove(direction, dest)
        case "/":
            moveDir = nextDirection[direction][0]
            beamMove(moveDir, dest)
        case "\\":
            moveDir = nextDirection[direction][1]
            beamMove(moveDir, dest)
        case "|":
            moveDir = nextDirection[direction][2]
            for move in moveDir:
                beamMove(move, dest)
        case "-":
            moveDir = nextDirection[direction][3]
            for move in moveDir:
                beamMove(move, dest)


beamMove("R", (-1, 0))
energizedCoordinates = set(coor[0] for coor in energizedCoordinates)
print(len(energizedCoordinates))
