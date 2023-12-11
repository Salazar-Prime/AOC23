import re


def getNumbersFromString(str):
    # returns a list of nubers from a string
    return [int(s) for s in re.findall(r"-?\d+", str)]


def saveToFile(data, saveName):
    # save to file
    with open(saveName, "w") as f:
        for line in data:
            f.write(line + "")
