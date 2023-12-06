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

raceTimes = getNumbersFromString(data[0])
raceDistances = getNumbersFromString(data[1])

result = 1
# loop for each race
for idx, raceTime in enumerate(raceTimes):
    # loop for itrating over varying button press duration
    possiblitites = 0
    for heldTime in range(1, raceTime):
        speed = heldTime
        disTravelled = speed * (raceTime - heldTime)
        if disTravelled > raceDistances[idx]:
            possiblitites += 1
    result *= possiblitites
print(result)
