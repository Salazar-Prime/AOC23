##### BEGIN BOIER CODE #####
import sys, os, re
from itertools import cycle
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 8
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####

instructions = data[0].strip()
instructtMap = {"L": 0, "R": 1}

# create a dictionary with first three letters as key and value as the tuple
dict = {}
for line in data[2:]:
    key = line[:3]
    val = line[5:].replace("(", "").replace(")", "").strip().split(", ")
    dict[key] = (val[0], val[1])


# get keyLIst with all keys ending in A
keyList = [key for key in dict.keys() if key[-1] == "A"]
countList = []
for key in keyList:
    count = 0
    iterator = cycle(instructions)
    while key[-1] != "Z":
        currentInstruct = next(iterator)
        key = dict[key][instructtMap[currentInstruct]]
        count += 1
    countList.append(count)

# take LCM of countLIst
print(lcm(countList))
