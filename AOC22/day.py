import inputs

data = inputs.getInput(1).split("\n")

idx = 0
sumList = []

for i in range(len(data)):
    if data[i] != "":
        continue
    subList = data[idx:i]
    # convert to int
    subList = list(map(int, subList))
    sumList.append(sum(subList))
    idx = i + 1

# sort
sumList.sort()
# add top 3
print(sumList[-1] + sumList[-2] + sumList[-3])
