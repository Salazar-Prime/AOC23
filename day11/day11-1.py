##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *
from itertools import combinations

sys.path.insert(1, "common")
from utils import *

test = False
currentDay = 11
if test:
    data = list(open(f"day{currentDay}/test.txt"))
    rowCount = 10
    colCount = 10
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
    rowCount = 140
    colCount = 140
##### END BOIER CODE #####

colIndex = list(range(rowCount))
rowIndex = list(range(colCount))
factor = 2

emptyColCount = 0
emptyRowCount = 0

# Get new updated for Rows/Y
for idx, row in enumerate(data):
    row = row.strip()
    rowIndex[idx] += emptyRowCount * (factor - 1)
    # count number of .
    if row.count(".") == rowCount:
        emptyRowCount += 1

# Get new updated index for Columns/X
for idx, col in enumerate(zip(*data)):
    col = "".join(col)
    colIndex[idx] += emptyColCount * (factor - 1)
    # count number of .
    if col.count(".") == colCount:
        print("Empty column Index + 1:", idx + 1)
        emptyColCount += 1

poundLocation = []
# get location of all # in the grid
for idx, row in enumerate(data):
    row = row.strip()
    for jdx, col in enumerate(row):
        if col == "#":
            poundLocation.append((rowIndex[idx], colIndex[jdx]))
# sort by first
poundLocation.sort(key=lambda x: x[0])

# find distane between each pair of # in the grid
# manhattan distance
poundLocationPairs = combinations(poundLocation, 2)

totalDistance = 0
for pair in poundLocationPairs:
    totalDistance += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

print(totalDistance)
