##### BEGIN BOIER CODE #####
import sys, os, re

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 1
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####
