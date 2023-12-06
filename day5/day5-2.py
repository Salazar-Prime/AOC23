import os, re
from utils import *

test = False
currentDay = 5
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))

# get seed numbers
seeds = list(map(int, re.findall(r"\d+", data[0])))
# seeds list has two pair of numbers. The first number is starting seed, the second number is number of seeds
seeds = zip(seeds[0::2], seeds[1::2])

# map: seed - soil - fetilizer - water - light - temperature - humodity - location
maps = [
    getMap(data, "seed-to-soil map:"),
    getMap(data, "soil-to-fertilizer map:"),
    getMap(data, "fertilizer-to-water map:"),
    getMap(data, "water-to-light map:"),
    getMap(data, "light-to-temperature map:"),
    getMap(data, "temperature-to-humidity map:"),
    getMap(data, "humidity-to-location map:"),
]

# destination, source, count
# time the code 
import time
start = time.time()
minLocation = findInMaps4SeedRangeSerial(maps, seeds, first=True)
print("complete serial in ", time.time() - start)
start = time.time()
minLocation = findInMaps4SeedRangeParallel(maps, seeds, first=True)
print("complete serial in ", time.time() - start)
# print(minLocation)
