def getSymmDiff(grid, index):
    numRows = min(index + 1, len(grid) - index - 1)
    upperGrid = grid[index + 1 - numRows : index + 1][-1::-1]
    lowerGrid = grid[index + 1 : index + numRows + 1]

    offBy = 0
    for idx, row in enumerate(upperGrid):
        for jdx, char in enumerate(row):
            if char != lowerGrid[idx][jdx]:
                offBy += 1
    return offBy
