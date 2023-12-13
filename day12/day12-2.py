##### BEGIN BOIER CODE #####
import sys, os, re, time
from localUtils import *
import itertools

sys.path.insert(1, "common")
from utils import *

test = False
currentDay = 12
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####

timeCode = False
factor = 5
count = 0
if timeCode:
    startTime = time.time()
for idx, line in enumerate(data):
    print(f"processing line {idx}")
    pattern, hashStr = line.split()
    hashCounts = getNumbersFromString(hashStr)
    pattern, hashCounts = pattern * factor, hashCounts * factor
    for combination in itertools.product([".", "#"], repeat=pattern.count("?")):
        # print(combination)
        newPattern = pattern
        for char in combination:
            newPattern = newPattern.replace("?", char, 1)
        # get total number os hash in newPattern
        totalHash = newPattern.count("#")
        if totalHash != sum(hashCounts) or totalHash == 0:
            continue
        if getHashCounts(tuple(newPattern)) == hashCounts:
            count += 1

if timeCode:
    timeTaken = time.time() - startTime
    print(f"Time taken: {timeTaken}")
print(count)