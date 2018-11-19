from point import Point, distance
from rectangle import Rectangle
import copy


class Circle:
    ''' Represents a circle
    Attributes center and radius
    '''


def point_in_circle(circle, point):
    ''' Checks whether a point lies inside a circle (or on the boundary)'''
    d = distance(circle.center, point)
    if d <= circle.radius:
        return True
    return False


def rect_in_circle(circle, rect):
    ''' Checks whether the corners of a rect fall in/on a circle'''
    temp = copy.copy(rect.corner)
    if not point_in_circle(circle, temp):
        return False

    temp.x += rect.width
    if not point_in_circle(circle, temp):
        return False

    temp.x -= rect.width
    if not point_in_circle(circle, temp):
        return False

    temp.y -= rect.height
    if not point_in_circle(circle, temp):
        return False

    return True


if __name__ == '__main__':
    circle = Circle()
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    circle.radius = 75

    p = Point()
    p.x = 225
    p.y = 100
    print(point_in_circle(circle, p))

    box = Rectangle()
    box.width = 100
    box.height = 200
    box.corner = Point()
    box.corner.x = 50
    box.corner.y = 50
    print(rect_in_circle(circle, box))
