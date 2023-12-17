##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 15
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))

data = "\n".join(data).split(",")
##### END BOIER CODE #####

boxes = {}
for i in range(256):
    boxes[i] = []

for hashStr in data:
    regex = re.compile(r"([a-z]+)([=-])(\d?)").match(hashStr)
    hash = getHash4Str(regex.group(1))
    box = boxes[hash]
    match regex.group(2):
        case "=":
            for idx, lens in enumerate(box):
                if lens.startswith(regex.group(1)):
                    box[idx] = regex.group(1) + " " + regex.group(3)
                    break
            else:
                box.append(regex.group(1) + " " + regex.group(3))
        case "-":
            for idx, lens in enumerate(box):
                if lens.startswith(regex.group(1)):
                    box.remove(lens)

result = 0
for boxNo, box in enumerate(boxes):
    for lensNo, lens in enumerate(boxes[box]):
        result += (boxNo + 1) * (lensNo + 1) * int(lens.split(" ")[1])

print(result)
