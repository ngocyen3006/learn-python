import abc
import math


class Shape:
    '''
    Shape is abstract base class
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, metaclass):
        self.__metaclass__ = metaclass


class Circle(Shape):
    '''
    This a circle class
    '''

    def __init__(self, r):
        self.r = r

    def circumference(self):
        return 2 * self.r * math.pi

    def area(self):
        return math.pi * (self.r ** 2)

    def print_info(self):
        print(f'Circumference: {self.circumference():.2f}')
        print(f'Area: {self.area():.2f}')


class Rectangle(Shape):
    '''
    This is a rectangle class
    '''

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def perimeter(self):
        return 2 * (self.l + self.w)

    def area(self):
        return self.l * self.w

    def print_info(self):
        print(f'Perimeter: {self.perimeter():.2f}')
        print(f'Area: {self.area():.2f}')


class Triangle(Shape):
    '''
    This is triangle class
    '''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        h = self.perimeter() / 2
        return math.sqrt(h * (h - self.a) * (h - self.b) * (h - self.c))

    def print_info(self):
        print(f'Perimeter: {self.perimeter():.2f}')
        print(f'Area: {self.area():.2f}')


class InputInfo:
    def __init__():
        pass

    def input_circle():
        r = int(input('Input radius: '))
        return r

    def input_rec():
        l = int(input('Input length: '))
        w = int(input('Input width: '))
        c = [l, w]
        return c

    def input_tri():
        a = int(input('Input a: '))
        b = int(input('Input b: '))
        c = int(input('Input c: '))
        l = [a, b, c]
        return l


if __name__ == '__main__':
    loop = int(input('Choose: 0: None, 1: Circle, 2: Rectangle, 3: Triangle'))
    while loop > 0:
        if loop == 1:
            r = InputInfo.input_circle()
            circle = Circle(r)
            circle.print_info()
        elif loop == 2:
            re = InputInfo.input_rec()
            rec = Rectangle(re[0], re[1])
            rec.print_info()
        else:
            tr = InputInfo.input_tri()
            tri = Triangle(tr[0], tr[1], tr[2])
            tri.print_info()

        loop = int(input('Choose: 0: None, 1: Circle, 2: Rectangle, 3: Triangle'))
