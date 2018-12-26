# https://www.codewars.com/kata/bit-counting/train/python

def countBits(n):
    b = bin(n)[2:]
    return sum([int(i) for i in b])
