##### BEGIN BOIER CODE #####
# fmt: off
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 23
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))

# Convert to numpy array Str/Int
# data = convertToNumpyArray(data, dtype=str)
# create a grid dicitonary od data with coordinates as keys and data as values
# grid, gridW, gridH = gridify(data, int)

# fmt:on
##### END BOIER CODE #####
