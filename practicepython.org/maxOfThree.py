# http://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

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
