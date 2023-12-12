import re, functools


@functools.cache
def checkValidPattern(pattern, hashCountList):
    pattern = "".join(pattern)
    return [len(match) for match in re.findall(r"#+", pattern)] == list(hashCountList)


@functools.cache
def getHashCounts(pattern):
    pattern = "".join(pattern)
    return [len(match) for match in re.findall(r"#+", pattern)]
