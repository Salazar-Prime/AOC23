def getHash4Str(hashStr):
    result = 0
    for char in hashStr:
        # get ASCII value of char
        result += ord(char)
        result *= 17
        result %= 256
    return result
