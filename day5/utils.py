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


# def findInMaps4SeedRange(maps, seeds, first=False):
#     for startSeed, count in seeds:
#         for seed in range(startSeed, startSeed + count):
#             location = findInMaps(maps, seed)
#         if first:
#             break
#     return location


def findInMaps4SeedRange(maps, seeds, first=False):
    results = []
    minLocation = 0
    for startSeed, count in seeds:
        # Using ThreadPoolExecutor to parallelize the function calls
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks to the executor and store the Future objects in a list
            futures = [
                executor.submit(findInMaps, maps, i)
                for i in range(startSeed, startSeed + count)
            ]

            # Wait for all tasks to complete and retrieve the results
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"An exception occurred: {e}")

        if first:
            minLocation = min(results)
            print("Complete")
            return minLocation
            break
        if len(results) > 0 and min(results) < minLocation:
            minLocation = min(results)
