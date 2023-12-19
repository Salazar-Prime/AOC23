##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *
from queue import PriorityQueue

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 17
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))

# Convert to numpy array Str
# data = convertToNumpyArrayStr(data)
# Convert to numpy array Int
# data = convertToNumpyArrayInt(data)

grid = {(x, y): int(c) for y, r in enumerate(data) for x, c in enumerate(r.strip("\n"))}
gridW = max(x for x, y in grid.keys()) + 1
gridH = max(y for x, y in grid.keys()) + 1

##### END BOIER CODE #####
# EG: getGridNeighbors(grid, (0, 0))
minStraight = 1
maxStraight = 3
directions = {(0, -1), (1, 0), (0, 1), (-1, 0)}  # N, E, S, W
# create a frontier
frontier = PriorityQueue()
# queue tuple: cost, nX, nY, pX, pY
start = (0, 0)
goal = (gridW - 1, gridH - 1)
frontier.put((0, start[0], start[1], 0, 0))

explored = set()

while not frontier.empty():
    cost, nX, nY, pX, pY = frontier.get()

    if (nX, nY) == goal:
        break  # found goal
    if (nX, nY, pX, pY) in explored:
        continue  # already explored node
    explored.add((nX, nY, pX, pY))

    # Can't go back the way we came (px, pY) or move more in same direction (-px, -pY)
    for direction in directions - {(pX, pY), (-pX, -pY)}:
        # initialize neighbor and costTemp for each direction
        neighbor, costTemp = (nX, nY), cost
        for distance in range(1, maxStraight + 1):
            # move by 1
            neighbor = addT(neighbor, direction)
            if (neighbor) in grid:
                # Keeps a running total of cost away from nX, nY
                costTemp += grid[neighbor]
                if distance >= minStraight:
                    frontier.put((costTemp, *neighbor, *direction))
print(cost)
