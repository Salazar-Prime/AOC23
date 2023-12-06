##### BEGIN BOIER CODE #####
import sys, os, re

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 6
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####

raceTime = int("".join([str(x) for x in getNumbersFromString(data[0])]))
raceDistance = int("".join([str(x) for x in getNumbersFromString(data[1])]))

result = 1
firstTimeFlag = True
possiblitites = 0
for heldTime in range(1, raceTime):
    speed = heldTime
    disTravelled = speed * (raceTime - heldTime)
    if disTravelled > raceDistance:
        firstTimeFlag = False
        possiblitites += 1
    # for breaking early - gaussian thing
    elif disTravelled < raceDistance and not firstTimeFlag:
        break
result *= possiblitites
print(result)
