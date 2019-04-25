# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError

    positive = (dividend < 0) is (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0

    while divisor <= dividend:
        temp = divisor
        i = 1
        while temp <= dividend:
            dividend -= temp
            count += i
            i <<= 1
            temp <<= 1

    if not positive:
        count = -count

    return min(max(-2147483648, count), 2147483647)

