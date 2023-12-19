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
data = [getHexCodeFromString(line[2], False)for line in (line.strip().split(" ") for line in data)]
data = [[int(line[:-1], 16), line[-1]] for line in data]
# fmt:on
##### END BOIER CODE #####

# 0 means R, 1 means D, 2 means L, and 3 means U.
directions = {"3": (0, -1), "1": (0, 1), "2": (-1, 0), "0": (1, 0)}
currentCoord = (0, 0)
polygonCoords = []

for line in data:
    movDirection, movDistance = directions[line[1]], line[0]
    currentCoord = addT(currentCoord, mulTConst(movDirection, movDistance))
    polygonCoords.append(currentCoord)
polygon = Polygon(polygonCoords)

# # https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdveugr/
print("Total Area: ", polygon.area + polygon.boundary.length / 2 + 1)
