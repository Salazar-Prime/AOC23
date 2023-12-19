import re
import numpy as np


def mulTConst(a, b):
    # check if a is a tuple and b is a constant
    if not isinstance(a, tuple) or not isinstance(b, int):
        raise TypeError("a must be a tuple and b must be a constant")
    if b == 1:
        return a
    return tuple(x * b for x in a)


def mulTwithT(a, b):
    # check if a and b are tuples and equal length
    if not isinstance(a, tuple) or not isinstance(b, tuple):
        raise TypeError("a and b must be tuples")
    if len(a) != len(b):
        raise ValueError("a and b must be of equal length")
    return tuple(x * y for x, y in zip(a, b))


def addT(a, b):
    # check if a and b are tuples and equal length
    if not isinstance(a, tuple) or not isinstance(b, tuple):
        raise TypeError("a and b must be tuples")
    if len(a) != len(b):
        raise ValueError("a and b must be of equal length")
    return tuple(sum(x) for x in zip(a, b))


def getNumbersFromString(str):
    # returns a list of nubers from a string
    return [int(s) for s in re.findall(r"-?\d+", str)]


# fmt: off
def gridify(data, dtype = str ):
    if dtype == int:
        grid = {(x, y): int(c) for y, r in enumerate(data) for x, c in enumerate(r.strip("\n"))}
    elif dtype == str:
        grid = {(x, y): c for y, r in enumerate(data) for x, c in enumerate(r.strip("\n"))}
    gridW = max(x for x, y in grid.keys()) + 1
    gridH = max(y for x, y in grid.keys()) + 1
    return grid, gridW, gridH

def convertToNumpyArray(data, removeNewLine=True, dtype=str):
    # get length of each row and total number of rows
    totalRows = len(data)
    totalCols = len(data[0])
    if removeNewLine:
        totalCols -= 1
    # create numpy array
    arr = np.zeros((totalRows, totalCols), dtype=dtype)
    # populate numpy array
    for idx, row in enumerate(data):
        for jdx, char in enumerate(row):
            if removeNewLine and char == "\n":
                continue
            arr[idx][jdx] = char
    return arr

def saveToFile(data, saveName, newLine=True):
    # save to file
    with open(saveName, "w") as f:
        for line in data:
            if newLine:
                f.write(line + "\n")
            else:
                f.write(line + "")

# Legacy code
def convertToNumpyArrayInt(data, removeNewLine=True):
    return convertToNumpyArray(data, removeNewLine, int)
def convertToNumpyArrayStr(data, removeNewLine=True):
    return convertToNumpyArray(data, removeNewLine, str)
