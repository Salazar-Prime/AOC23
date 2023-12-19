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


def convertToNumpyArrayStr(data, removeNewLine=True):
    # get length of each row and total number of rows
    totalRows = len(data)
    totalCols = len(data[0])
    if removeNewLine:
        totalCols -= 1
    # create numpy array
    arr = np.zeros((totalRows, totalCols), dtype=str)
    # populate numpy array
    for idx, row in enumerate(data):
        for jdx, char in enumerate(row):
            if removeNewLine and char == "\n":
                continue
            arr[idx][jdx] = char
    return arr


def convertToNumpyArrayInt(data, removeNewLine=True):
    # get length of each row and total number of rows
    totalRows = len(data)
    totalCols = len(data[0])
    if removeNewLine:
        totalCols -= 1
    # create numpy array
    arr = np.zeros((totalRows, totalCols), dtype=int)
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
