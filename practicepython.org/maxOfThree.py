def maxOfTwo(a, b):
    try:
        if a > b:
            return a
        return b
    except TypeError:
        return


def maxOfThree(a, b, c):
    maxTwo = maxOfTwo(a, b)
    maxVariable = maxOfTwo(maxTwo, c)
    return maxVariable
