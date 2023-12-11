##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
# test = True
currentDay = 9
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####

nextNumberSum = 0
for line in data:
    arr = getNumbersFromString(line.strip())
    sum = arr[-1]
    while True:
        diffArray = getDiffArray(arr)
        sum += diffArray[-1]
        absSum = getAbsSum(diffArray)
        if absSum == 0:
            break
        else:
            arr = diffArray
    nextNumberSum += sum
print(nextNumberSum)
