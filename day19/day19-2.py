##### BEGIN BOIER CODE #####
# fmt: off
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *
sys.setrecursionlimit(10000)

test = False
currentDay = 19
if test:
    data = open(f"day{currentDay}/test.txt").read()
else:
    data = open(f"day{currentDay}/day{currentDay}-1.txt").read()
workflows, parts = data.split("\n\n")
workflows = {m[0]: m[1].split(",") for m in re.compile(r"(\w+){(.*)}").findall(workflows)}

# Convert to numpy array Str/Int
# data = convertToNumpyArray(data, dtype=str)
# create a grid dicitonary od data with coordinates as keys and data as values
# grid, gridW, gridH = gridify(data, int)
# fmt:on
##### END BOIER CODE #####
partMapping = {"x": 0, "m": 1, "a": 2, "s": 3}
acceptableParts = []


def getNextWorkflow(workflow, partStats):
    if workflow == "A":
        acceptableParts.append(partStats)
        return 0
    if workflow == "R":
        return 0
    for step in workflows[workflow]:
        match = re.compile(r"(\w+)([<>]?)(\d*):?(\w*)").match(step)
        if match.group(2) == "":
            getNextWorkflow(match.groups()[0], partStats)
        else:
            statName, operator, statVal, nextWorkflow = match.groups()
            if operator == "<":
                splitPoint = int(statVal)
                newPartStats = partStats.copy()
                newPartStats[partMapping[statName]] = (
                    partStats[partMapping[statName]][0],
                    splitPoint - 1,
                )
                getNextWorkflow(nextWorkflow, newPartStats)
                partStats[partMapping[statName]] = (
                    splitPoint,
                    partStats[partMapping[statName]][1],
                )
            elif operator == ">":
                splitPoint = int(statVal)
                newPartStats = partStats.copy()
                newPartStats[partMapping[statName]] = (
                    splitPoint + 1,
                    partStats[partMapping[statName]][1],
                )
                getNextWorkflow(nextWorkflow, newPartStats)
                partStats[partMapping[statName]] = (
                    partStats[partMapping[statName]][0],
                    splitPoint,
                )


partStats = [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]
getNextWorkflow("in", partStats)

total = 0
for part in acceptableParts:
    count = 1
    for p in part:
        count *= p[1] - p[0] + 1
    total += count
print(total)
