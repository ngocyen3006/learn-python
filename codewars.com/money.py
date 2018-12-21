# https://www.codewars.com/kata/money-money-money/train/python

def calculate_years(p, i, t, d):
    y = 0
    while p < d:
        I = p * i
        T = I * t
        p = p + I - T
        y += 1
    return y


print(calculate_years(1000, 0.05, 0.18, 1100))
