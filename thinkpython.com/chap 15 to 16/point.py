import math


class Point:
    ''' Represents a point in 2-D space.'''


def distance(p1, p2):
    ''' Computes the distance between two Point objects'''
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    d = math.sqrt(dx ** 2 + dy ** 2)
    return d
