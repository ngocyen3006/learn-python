# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError

    d = 1
    s = 1
    if dividend < 0:
        d = -1
    if divisor < 0:
        s = -1

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

    if d == -1 and s == 1 or s == -1 and d == 1:
        count = -count

    return min(max(-2147483648, count), 2147483647)


dvd = 7
dvs = 3
print(divide(dvd, dvs))
