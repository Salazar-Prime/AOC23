import os, re
from localUtils import *

test = False
currentDay = 5
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))

# get seed numbers
seeds = list(map(int, re.findall(r"\d+", data[0])))

# map: seed - soil - fetilizer - water - light - temperature - humodity - location
seed2soil = getMap(data, "seed-to-soil map:")
soil2fertilizer = getMap(data, "soil-to-fertilizer map:")
fertilizer2water = getMap(data, "fertilizer-to-water map:")
water2light = getMap(data, "water-to-light map:")
light2temperature = getMap(data, "light-to-temperature map:")
temperature2humidity = getMap(data, "temperature-to-humidity map:")
humidity2location = getMap(data, "humidity-to-location map:")

maps = [
    seed2soil,
    soil2fertilizer,
    fertilizer2water,
    water2light,
    light2temperature,
    temperature2humidity,
    humidity2location,
]
# destination, source, count
minLocation = findInMaps(maps, seeds[0])
for seed in seeds[1:]:
    location = findInMaps(maps, seed)
    if location < minLocation:
        minLocation = location

print(minLocation)
