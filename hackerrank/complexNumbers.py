# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imag + no.imag)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imag - no.imag)

    def __mul__(self, no):
        r = self.real * no.real - self.imag * no.imag
        i = self.real * no.imag + no.real * self.imag
        return Complex(r, i)

    def __truediv__(self, no):
        return self.__mul__(Complex(no.real, -1 * no.imag)). \
            __mul__(Complex(1.0 / (no.mod().real) ** 2, 0))

    def mod(self):
        return Complex(pow(self.real ** 2 + self.imag ** 2, 0.5), 0)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result


# Method 2
# class Complex(complex):
#     def __add__(self, no):
#         return Complex(complex.__add__(self, no))
#
#     def __sub__(self, no):
#         return Complex(complex.__sub__(self, no))
#
#     def __mul__(self, no):
#         return Complex(complex.__mul__(self, no))
#
#     def __truediv__(self, no):
#         return Complex(complex.__truediv__(self, no))
#
#     def mod(self):
#         return Complex(complex.__abs__(self))
#
#     def __str__(self):
#         return '{0.real:.2f}{0.imag:+.2f}i'.format(self)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
