# fmt: off
# get all files in current folder
import os, re, shutil
from aoc import aoc

# get list of all folders in current directory that start with day
folders = filter(lambda a: a.startswith("day"), os.listdir("."))
# get max day number
maxDay = max(map(lambda a: re.search(r"\d+", a).group(), folders))

# create new day folder
newDay = "day" + str(int(maxDay) + 1)
os.mkdir(newDay)

# create new day python files day{newDay}-1.py and day{newDay}-2.py
open(newDay + "/day" + newDay + "-1.py", "w+")
open(newDay + "/day" + newDay + "-2.py", "w+")

# copy content of template.py to day{newDay}-1.py
template = open("template.py").read()
template = template.replace("currentDay = 1", "currentDay = " + str(int(maxDay) + 1))
# write template to day{newDay}-1.py
open(newDay + "/day" + newDay + "-1.py", "w+").write(template)
open(newDay + "/day" + newDay + "-2.py", "w+").write(template)

# get input from AOC website
from aoc import aoc
temp = aoc.get_input(5)
os.rename("data/2023" + "_" + str(int(maxDay) + 1) + ".txt", newDay + "/day" + newDay + "-1.txt")

# delete all files in data folder and then delete data folder
shutil.rmtree('data')
