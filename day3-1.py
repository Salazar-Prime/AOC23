import re

# 140 x 140 grid
# Sample line text: .......153..988....502..842......

board = list(open("inputs/day3-1.txt"))
# get location of all characters
charLocs = {
    (r, c): []
    for r in range(140)
    for c in range(140)
    if board[r][c] not in "0123456789."
}

for r, row in enumerate(board):
    for num in re.finditer(r"\d+", row):
        edges = {
            (r, c)
            for r in (r - 1, r, r + 1)
            for c in range(num.start() - 1, num.end() + 1)
        }

        for o in edges & charLocs.keys():
            charLocs[o].append(int(num.group()))

# get sum of all numbersprint
print(sum(sum(v) for v in charLocs.values()))
