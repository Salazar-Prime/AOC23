import sys

sys.path.insert(1, "common")
from utils import *


def getGridNeighbors(grid, node, distFrom=1):
    neighbors = []

    def addNeighbor(neighbor):
        if (
            neighbor[0] >= 0
            and neighbor[0] < len(grid[0])
            and neighbor[1] >= 0
            and neighbor[1] < len(grid)
        ):
            neighbors.append(neighbor)

    # node has two compoenents, x and y
    addNeighbor(addT(node, mulTConst((0, -1), distFrom)))  # NORTH
    addNeighbor(addT(node, mulTConst((0, 1), distFrom)))  # SOUTH
    addNeighbor(addT(node, mulTConst((-1, 0), distFrom)))  # WEST
    addNeighbor(addT(node, mulTConst((1, 0), distFrom)))  # EAST
    return neighbors
