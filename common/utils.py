import re


def getNumbersFromString(str):
    # returns a list of nubers from a string
    return [int(s) for s in re.findall(r"-?\d+", str)]


def saveToFile(data, saveName, newLine=True):
    # save to file
    with open(saveName, "w") as f:
        for line in data:
            if newLine:
                f.write(line + "\n")
            else:
                f.write(line + "")
