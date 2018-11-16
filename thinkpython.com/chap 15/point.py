import math


class Point:
    ''' Represents a point in 2-D space.'''


def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)


blank = Point()
blank.x = 3.0
blank.y = 4.0
print(distance(blank.x, blank.y))
