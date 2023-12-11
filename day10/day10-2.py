##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 10
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####


data = list(open("day10/part1-map.txt"))
# replace all but O with " "
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != "O" and char != "\n":
            data[y] = replaceChar(data[y], " ", x)

# SSCAN FROM LEFT
for y in range(140):
    for x in range(140):
        if data[y][x] != "O":
            data[y] = replaceChar(data[y], "X", x)
        else:
            break

# SCAN FROM RIGHT
for y in range(140):
    # rever range for 140
    for x in range(139, -1, -1):
        if data[y][x] != "O":
            data[y] = replaceChar(data[y], "X", x)
        else:
            break

# SCAN FROM TOP
for x in range(140):
    for y in range(140):
        if data[y][x] != "O":
            data[y] = replaceChar(data[y], "X", x)
        else:
            break
668
# SCAN FROM BOTTOM
for x in range(140):
    for y in range(139, -1, -1):
        if data[y][x] != "O":
            data[y] = replaceChar(data[y], "X", x)
        else:
            break

# LOOP OVER DATA and count " "
count = 0
for idx, line in enumerate(data):
    print("Line Number: ", idx + 1)
    for idy, char in enumerate(line):
        if char == " ":
            # check if its top, bottom, left or right neighbour is "X"
            if (
                data[idx - 1][idy] == "X"
                or data[idx + 1][idy] == "X"
                or data[idx][idy - 1] == "X"
                or data[idx][idy + 1] == "X"
            ):
                # replace with X
                data[idx] = replaceChar(data[idx], "X", idy)

for line in data:
    for char in line:
        if char == " ":
            count += 1
print(count)
# save to file
saveToFile(data, "day10/part2-map.txt")
