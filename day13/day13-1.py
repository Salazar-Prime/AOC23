##### BEGIN BOIER CODE #####
import sys, os, re
import numpy as np
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 13
# fmt: off
if test:
    data = list(map(str.split, open(f"day{currentDay}/test.txt").read().split("\n\n")))
else:
    data = list(map(str.split,open(f"day{currentDay}/day{currentDay}-1.txt").read().split("\n\n")))
##### END BOIER CODE #####
# fmt: on

conditionDiff = 0
result = 0

for group in data:
    for idx in range(len(group) - 1):
        if getSymmDiff(group, idx) == conditionDiff:
            result += 100 * (idx + 1)

# swap row and col of data
transposedData = []
for group in data:
    transposedData.append(list(map(list, zip(*group))))
data = transposedData

for group in data:
    for idx in range(len(group) - 1):
        if getSymmDiff(group, idx) == conditionDiff:
            result += 1 * (idx + 1)

print(result)