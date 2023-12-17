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

total = 0
for hashStr in data:
    total += getHash4Str(hashStr)
print(total)
