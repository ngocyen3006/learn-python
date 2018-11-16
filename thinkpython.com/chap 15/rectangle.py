from point import Point


class Rectangle:
    ''' Represents a rectangle.
        attributes: width, height, corner.
    '''


def find_center(box):
    '''Returns a Point at the center of a Rectangle.'''
    p = Point()
    p.x = box.corner.x + box.width / 2.0
    p.y = box.corner.y + box.height / 2.0
    return p


def print_point(p):
    '''Print a Point object in human-readable format.'''
    print('(%g, %g)' % (p.x, p.y))


def grow_rectangle(rect, dwidth, dheight):
    '''Modifies the Rectangle by adding to its width and height.'''
    rect.width += dwidth
    rect.height += dheight


def move_rectangle(rect, dx, dy):
    '''Move the Rectangle by modifying its corner object.'''
    rect.corner.x += dx
    rect.corner.y += dy
