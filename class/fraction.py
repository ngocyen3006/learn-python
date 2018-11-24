def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Fraction:
    def __init__(self, numerator, denominator):
        self.numer = numerator
        if denominator == 0:
            raise ValueError
        self.den = denominator

    def __str__(self):
        return str(self.numer) + "/" + str(self.den)

    def __add__(self, other):
        numer = self.numer * other.den + self.den * other.numer
        den = self.den * other.den
        res = Fraction(numer, den)
        return res.SimplifyFraction()

    def SimplifyFraction(self):
        GCD = gcd(self.numer, self.den)
        return Fraction(self.numer // GCD, self.den // GCD)


if __name__ == "__main__":
    f1 = Fraction(2, 3)
    print(f"Fraction 1: {f1}")

    f2 = Fraction(4, 5)
    print(f"Fraction 2: {f2}")

    f3 = Fraction(1, 2)
    print(f"Fraction 3: {f3}")
    f = f1 + f2 + f3
    print(f"Sum is: {f}")
