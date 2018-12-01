import abc
import math


class Shape:
    '''
    Shape is abstract base class
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass

    def print_attribute(self):
        pass

    def print_info(self):
        print("*" * 30)
        print("Name:", self.name)
        self.print_attribute()
        print(f"Perimeter: {self.perimeter():.2f}")
        print(f"Area: {self.area():.2f}")
        print('*' * 30)


class Circle(Shape):
    '''
    This a circle class
    '''

    def __init__(self, name, r):
        Shape.__init__(self, name)
        self.r = r

    def perimeter(self):
        return 2 * self.r * math.pi

    def area(self):
        return math.pi * (self.r ** 2)

    def print_attribute(self):
        print(f'Radius: {self.r}')


class Rectangle(Shape):
    '''
    This is a rectangle class
    '''

    def __init__(self, name, l, w):
        Shape.__init__(self, name)
        self.l = l
        self.w = w

    def perimeter(self):
        return 2 * (self.l + self.w)

    def area(self):
        return self.l * self.w

    def print_attribute(self):
        print(f'Length: {self.l}')
        print(f'Width: {self.w}')


class Triangle(Shape):
    '''
    This is triangle class
    '''

    def __init__(self, name, a, b, c):
        Shape.__init__(self, name)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        h = self.perimeter() / 2
        return math.sqrt(h * (h - self.a) * (h - self.b) * (h - self.c))

    def print_attribute(self):
        print(f'a: {self.a}')
        print(f'b: {self.b}')
        print(f'c: {self.c}')


class InputInfo:
    def __init__():
        pass

    def input_circle():
        name = input('Input shape name: ')
        r = int(input('Input radius: '))
        c = [name, r]
        return c

    def input_rec():
        name = input('Input shape name: ')
        l = int(input('Input length: '))
        w = int(input('Input width: '))
        c = [name, l, w]
        return c

    def input_tri():
        name = input('Input shape name: ')
        a = int(input('Input a: '))
        b = int(input('Input b: '))
        c = int(input('Input c: '))
        l = [name, a, b, c]
        return l


if __name__ == '__main__':
    loop = int(input('Choose: 0: None, 1: Circle, 2: Rectangle, 3: Triangle'))
    while loop > 0:
        if loop == 1:
            r = InputInfo.input_circle()
            circle = Circle(r[0], r[1])
            circle.print_info()
        elif loop == 2:
            re = InputInfo.input_rec()
            rec = Rectangle(re[0], re[1], re[2])
            rec.print_info()
        else:
            tr = InputInfo.input_tri()
            tri = Triangle(tr[0], tr[1], tr[2], tr[3])
            tri.print_info()

        loop = int(input('Choose: 0: None, 1: Circle, 2: Rectangle, 3: Triangle'))
