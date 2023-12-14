##### BEGIN BOIER CODE #####
import sys, os, re
from localUtils import *

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 14
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####
