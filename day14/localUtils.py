def getDataTranspose(data):
    data = list(map(list, zip(*data)))
    # concatenate each row of data
    for i in range(len(data)):
        data[i] = "".join(data[i])
    return data


def getLoad(data):
    load = 0
    for d in data:
        for jdx, char in enumerate(d):
            if char == "O":
                load += len(d) - jdx
    return load


def tilt(data, otherDirection=False):
    for idx, d in enumerate(data):
        while True:
            if otherDirection:
                newData = d.replace("O.", ".O")
            else:
                newData = d.replace(".O", "O.")
            if newData == d:
                break
            d = newData
        data[idx] = d
    return data


def tiltCycle(data):
    # NORTH Tilt
    print("".join(data))
    data = tilt(data)
    print("After North Tilt")
    print("".join(data))
    # WEST Tilt
    data = getDataTranspose(data)
    data = tilt(data)
    print("After West Tilt")
    print("".join(data))
    # SOUTH Tilt
    data = getDataTranspose(data)
    data = tilt(data, True)
    print("After South Tilt")
    print("".join(data))
    # EAST Tilt
    data = getDataTranspose(data)
    data = tilt(data, True)
    print("After East Tilt")
    print("".join(data))
    return data
