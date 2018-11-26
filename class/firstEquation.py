class Equation:
    '''
    Represent for ax + b = 0
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        op = "+"
        if self.b < 0:
            op = "-"
        return f"{self.a}x {op} {abs(self.b)} = 0"

    def solve(self):
        if self.a == 0 and self.b != 0:
            return "Contrary equation"
        if self.a == 0 and self.b == 0:
            return "Identity equation"
        return -self.b / self.a

    def result(self):
        print(self.solve())
