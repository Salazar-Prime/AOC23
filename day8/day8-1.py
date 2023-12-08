##### BEGIN BOIER CODE #####
import sys, os, re
from itertools import cycle

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

count = 0
key = "AAA"
iterator = cycle(instructions)
while key != "ZZZ":
    currentInstruct = next(iterator)
    key = dict[key][instructtMap[currentInstruct]]
    count += 1
    if key == "ZZZ":
        break

print(count)
