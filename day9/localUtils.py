def getDiffArray(arr):
    diffArray = []
    for i in range(1, len(arr)):
        diffArray.append(arr[i] - arr[i - 1])
    return diffArray


def getAbsSum(arr):
    sum = 0
    for i in arr:
        sum += abs(i)
    return sum
