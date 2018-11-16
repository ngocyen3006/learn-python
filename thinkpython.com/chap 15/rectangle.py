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


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
center = find_center(box)
print_point(center)
grow_rectangle(box, 50, 100)
move_rectangle(box, 4.0, 4.0)
print_point(box.corner)
