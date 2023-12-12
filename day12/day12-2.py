##### BEGIN BOIER CODE #####
import sys, os, re
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

factor = 5
count = 0
for idx, line in enumerate(data):
    print(f"processing line {idx}")
    pattern, hashStr = line.split()
    hashCounts = getNumbersFromString(hashStr)
    pattern, hashCounts = pattern * factor, tuple(hashCounts * factor)
    iterProd = itertools.product([".", "#"], repeat=pattern.count("?"))
    print("Total combinations:", len(list(iterProd)))
    for combination in itertools.product([".", "#"], repeat=pattern.count("?")):
        newPattern = pattern
        for char in combination:
            newPattern = newPattern.replace("?", char, 1)
        if checkValidPattern(tuple(newPattern), hashCounts):
            count += 1

print(count)
