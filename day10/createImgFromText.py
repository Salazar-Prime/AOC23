import numpy as np

# read input
data = list(open("day10/part1-map.txt", "r"))
img = np.zeros((140, 140))

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "\n":
            continue
        if char == "O":
            img[i][j] = 1
        else:
            img[i][j] = 0

# save image
import matplotlib.pyplot as plt

plt.imsave("day10/part1-map.png", img, cmap="gray")
