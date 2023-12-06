import re


def getNumbersFromString(str):
    # returns a list of nubers from a string
    return [int(s) for s in re.findall(r"\d+", str)]
