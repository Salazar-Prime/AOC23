##### BEGIN BOIER CODE #####
import sys, os, re
import numpy as np
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 13
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####
ps = list(map(str.split, data.split("\n\n")))

# split data into groups sepearted by \n
groups = []
startIdx = 0
for idx, line in enumerate(data):
    if line == "\n":
        groups.append(data[startIdx:idx])
        startIdx = idx + 1

result = 0
for gpIdx, group in enumerate(groups):
    foundSymmetry = False
    totalRows = len(group)
    for idx in range(totalRows - 1):
        if group[idx] == group[idx + 1]:
            # found a possible symmetry line
            foundSymmetry, startIdx, endIdx = True, idx - 1, idx + 2
            while foundSymmetry:
                if startIdx < 0 or endIdx >= totalRows:
                    break
                if group[startIdx] == group[endIdx]:
                    startIdx -= 1
                    endIdx += 1
                else:
                    foundSymmetry = False
        if foundSymmetry:
            result += 100 * (idx + 1)
            print("".join(group))
            print(f"found symmetry at {idx}")
            print("-" * 10)
            break

# take transpose of groups
transposedGroups = []
for group in groups:
    transposedGroups.append(list(map(list, zip(*group))))

# delete last element of each group
for group in transposedGroups:
    del group[-1]

for gpIdx, group in enumerate(transposedGroups):
    foundSymmetry = False
    totalRows = len(group)
    for idx in range(totalRows - 1):
        if group[idx] == group[idx + 1]:
            # found a possible symmetry line
            foundSymmetry, startIdx, endIdx = True, idx - 1, idx + 2
            while foundSymmetry:
                if startIdx < 0 or endIdx >= totalRows:
                    break
                if group[startIdx] == group[endIdx]:
                    startIdx -= 1
                    endIdx += 1
                else:
                    foundSymmetry = False
        if foundSymmetry:
            result += idx + 1
            # print("".join(group))
            print(f"found symmetry at {idx}")
            print("-" * 10)
            break
print(result)
