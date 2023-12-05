# parse each line in the file and find
# first number from left and right
import re

namesDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
# open file
with open("day1-1.txt") as f:
    # read file line by line
    for line in f:
        # remove newline character
        line = line.rstrip("\n")
        digitStr = ""
        digitStrIdx = len(line)
        for name in namesDigits:
            if name in line:
                if line.find(name) < digitStrIdx:
                    digitStr = name
                    digitStrIdx = line.find(name)

        # find index of first digit in the line with regex
        digitIntIdx = re.search(r"(\d)", line).start()

        if digitStrIdx < digitIntIdx:
            # find posiiton of digitStr in namesDigits
            left = namesDigits.index(digitStr) + 1
        else:
            left = re.search(r"(\d)", line).group(1)

        digitStr = ""
        digitStrIdx = -1
        # find index of first digit from right in the line with regex
        for name in namesDigits:
            if name in line:
                if line.rfind(name) > digitStrIdx:
                    digitStr = name
                    digitStrIdx = line.rfind(name)

        digitIntIdx = re.search(r"(\d)", line[::-1]).start()
        digitIntIdx = len(line) - digitIntIdx - 1
        if digitStrIdx > digitIntIdx:
            # find posiiton of digitStr in namesDigits
            right = namesDigits.index(digitStr) + 1
        else:
            right = re.search(r"(\d)", line[::-1]).group(1)

        # concatenate left and right umbers
        result = str(left) + str(right)
        # convert string to int
        sum += int(result)

print(sum)
