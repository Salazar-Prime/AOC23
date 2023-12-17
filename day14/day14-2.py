##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = True
currentDay = 14
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####

cycles = 1000000000
cycles = 1
for i in range(cycles):
    if i % 100000 == 0:
        print(getLoad(data))
    # print(i)
    data = tiltCycle(data)

print(getLoad(data))
