##### BEGIN BOIER CODE #####
# fmt: off
import sys, os, re
from localUtils import *
from shapely.geometry import Polygon

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 18
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))

# Convert to numpy array Str/Int
# data = convertToNumpyArray(data, dtype=str)
# create a grid dicitonary od data with coordinates as keys and data as values
# grid, gridW, gridH = gridify(data, int)
data = [[line[0],getNumbersFromString(line[1], False),getHexCodeFromString(line[2], False)]for line in (line.strip().split(" ") for line in data)]
# fmt:on
##### END BOIER CODE #####

directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
currentCoord = (0, 0)
polygonCoords = []

for line in data:
    movDirection, movDistance = directions[line[0]], line[1]
    currentCoord = addT(currentCoord, mulTConst(movDirection, movDistance))
    polygonCoords.append(currentCoord)
polygon = Polygon(polygonCoords)
# https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdveugr/
print("Total Area: ", polygon.area + polygon.boundary.length / 2 + 1)
