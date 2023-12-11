def visMap(data, pos):
    dataCopy = data.copy()
    # replace chacrter in dataCopy at tp with "O"
    dataCopy[pos[1]] = dataCopy[pos[1]][: pos[0]] + "O" + dataCopy[pos[1]][pos[0] + 1 :]
    # replace symvols oin dataCopy following zip
    translation_table = str.maketrans("|JL7F-", "│┘└┐┌─")
    # apply tranlastion table
    dataCopy = [line.translate(translation_table) for line in dataCopy]
    # save it to newMap.txt
    with open("newMap.txt", "w") as f:
        f.write("".join(dataCopy))


def addT(t1, t2, dataCopy):
    tp = tuple(map(sum, zip(t1, t2)))
    visMap(dataCopy, tp)
    return tp


# check if the next node is a valid node for Starting direction
def checkDir(pos, dir, symbolMap, directions, data):
    symbolNodes = symbolMap[data[pos[1]][pos[0]]]
    checkSubNode = directions.index(dir)
    if symbolNodes[checkSubNode] == 1:
        return True
    return False


# get next node/direction of travel
def getNextNode(pos, entryDir, symbolMap, directions, data):
    x, y = pos
    # get symbol nodes
    symbol = data[y][x]
    symbolNodes = symbolMap[data[y][x]]
    # get index of all ones
    ones = [i for i, x in enumerate(symbolNodes) if x == 1]
    ones.remove(directions.index(entryDir))
    # remove index directions[entryDir]
    return directions[ones[0]]
