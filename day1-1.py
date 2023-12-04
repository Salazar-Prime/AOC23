# parse each line in the file and find
# first number from left and right
import re

sum = 0
# open file
with open("inputs/day1-1.txt") as f:
    # read file line by line
    for line in f:
        # remove newline character
        line = line.rstrip("\n")
        # find first number from left in a string using regex
        left = re.search(r"(\d)", line).group(1)
        # find first number from right in a string using regex
        right = re.search(r"(\d)", line[::-1]).group(1)
        
        # concatenate left and right umbers
        result = left + right
        # convert string to int
        sum += int(result)
print(sum)
