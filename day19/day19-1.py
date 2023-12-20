##### BEGIN BOIER CODE #####
# fmt: off
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


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


def getNextWorkflow(workflow, partStats):
    for step in workflow:
        match = re.compile(r"(\w+)([<>]?)(\d*):?(\w*)").match(step)
        nonEmptyGroupCount = len([g for g in match.groups() if g])
        if nonEmptyGroupCount == 1:
            return match.group(0)
        elif nonEmptyGroupCount == 4:
            statName, operator, statVal, nextWorkflow = match.groups()
            if operator == "<":
                if partStats[partMapping[statName]] < int(statVal):
                    return nextWorkflow
            elif operator == ">":
                if partStats[partMapping[statName]] > int(statVal):
                    return nextWorkflow


acceptableParts = []
for part in parts.split("\n"):
    partStats = getNumbersFromString(part)
    workflow = "in"
    while workflow:
        workflow = getNextWorkflow(workflows[workflow], partStats)
        if workflow == "A":
            acceptableParts.append(part)
            break
        if workflow == "R":
            break

result = sum([sum(getNumbersFromString(part)) for part in acceptableParts])
print(result)
