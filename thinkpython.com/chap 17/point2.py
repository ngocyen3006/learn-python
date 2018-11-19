class Point:
    '''Represents a point in 2-D space.'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Point(self.x + other[0], self.y + other[1])

    def __radd__(self, other):
        return self.__add__(other)


if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(6, 8)
    print(p1)
    print(p2)
    print(p1 + p2)
    print(p1 + (6, 8))
    print((3, 4) + p2)
