import math
from functools import reduce


#  https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple
def lcm(arr):
    l = reduce(lambda x, y: (x * y) // math.gcd(x, y), arr)
    return l
