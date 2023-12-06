import concurrent.futures

##### BEGIN BOIER CODE #####
import sys, os, re

sys.path.insert(1, "common")
from utils import *


def getMap(data, mapName):
    mapName = mapName + "\n"
    data.append("\n")
    return list(
        map(
            str.strip,
            data[data.index(mapName) + 1 : data.index("\n", data.index(mapName))],
        )
    )


def findInMaps(maps, seed):
    for singleMap in maps:
        for line in singleMap:
            # dest, src, count = line.split(" ")
            # convert to int
            dest, src, count = int(dest), int(src), int(count)
            if seed in range(src, src + count):
                offset = dest - src
                seed = seed + offset
                break
    return seed


def convertStrCount2StrEnd(seeds):
    # seeds tuple
    # The first number is starting seed
    # the second number is number of seeds
    seeds = [(seed, seed + count - 1) for seed, count in seeds]
    # sort by start
    seeds = sorted(seeds, key=lambda x: x[0])
    return set(seeds)


def getNewSeedRange(overlapStart, overlapEnd, seed):
    seeds = set()
    seedStart, seedEnd = seed
    if seedStart < overlapStart:
        seeds.add((seedStart, overlapStart - 1))
    if seedEnd > overlapEnd:
        seeds.add((overlapEnd + 1, seedEnd))
    return seeds


def getMinSeedLocation(maps, seeds):
    for singleMap in maps:
        newSeeds = set()
        for line in singleMap:
            for seed in seeds.copy():
                dest, src, count = getNumbersFromString(line)
                overlapStart = max(seed[0], src)
                overlapEnd = min(seed[1], src + count - 1)
                if overlapStart > overlapEnd:
                    continue
                if overlapStart <= overlapEnd:
                    offset = dest - src
                    newSeeds.add((overlapStart + offset, overlapEnd + offset))
                    seeds.remove(seed)
                    seeds |= getNewSeedRange(overlapStart, overlapEnd, seed)
        seeds |= newSeeds
    return min(x[0] for x in list(seeds))
