# line format: Game <gameNo>: 1 red, 6 blue, 2 green; 8 red, 5 green, 4 blue; 4 blue, 2 red, 3 green

import re

rgb = {"red": 12, "green": 13, "blue": 14}


def colorCount(set, color):
    # find color in set
    if color in set:
        # get count of color
        count = re.search(r"(\d+) " + color, set).group(1)
    else:
        count = 0
    return int(count)


# read file and parse line by line
with open("inputs/day2-1.txt") as f:
    sum = 0
    skipLineFlag = False
    for line in f:
        # remove newline character
        line = line.rstrip("\n")
        #  get ganme number
        gameNo = re.search(r"Game (\d+):", line).group(1)
        # split at :
        subset = line.split(":")[1].split(";")
        for set in subset:
            # get count of each color
            # get red if it exists\
            if "red" in set and colorCount(set, "red") > rgb["red"]:
                skipLineFlag = True
                break
            # get green if it exists
            if "green" in set and colorCount(set, "green") > rgb["green"]:
                skipLineFlag = True
                break
            # get blue if it exists
            if "blue" in set and colorCount(set, "blue") > rgb["blue"]:
                skipLineFlag = True
                break

        if skipLineFlag:
            skipLineFlag = False
            continue
        sum += int(gameNo)

print(sum)
