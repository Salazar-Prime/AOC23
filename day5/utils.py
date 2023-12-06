import concurrent.futures


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
            dest, src, count = line.split(" ")
            # convert to int
            dest, src, count = int(dest), int(src), int(count)
            if seed in range(src, src + count):
                offset = dest - src
                seed = seed + offset
                break
    return seed


def findInMaps4SeedRangeSerial(maps, seeds, first=False):
    for startSeed, count in seeds:
        for seed in range(startSeed, startSeed + count):
            location = findInMaps(maps, seed)
        if first:
            print("Complete Serial")
            break
    return location

def findInMaps4SeedRangeParallel(maps, seeds, first=False):
    def process_seed_range(startSeed, count):
        return [findInMaps(maps, i) for i in range(startSeed, startSeed + count)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = executor.map(lambda args: process_seed_range(*args), seeds)

    if first:
        return min(list(futures)) if results else None

    return min(list(futures), default=None)

