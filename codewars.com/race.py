# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

import unittest
import random
from math import floor, ceil


def race(v1, v2, g):
    time = []
    if v1 >= v2:
        return None
    s = v2 - v1
    t = g / s
    for _ in range(3):
        time.append(int(t))
        t = (t - int(t)) * 60
    return time


class TestRace(unittest.TestCase):
    def test_self(self):
        self.assertEqual(race(720, 850, 70), [0, 32, 18])
        self.assertEqual(race(80, 91, 37), [3, 21, 49])
        self.assertEqual(race(80, 100, 40), [2, 0, 0])


if __name__ == '__main__':
    for i in range(30):
        v1 = random.randint(50, 10000)
        v2 = random.randint(100, 10000)
        g = random.randint(30, 150)
        print(f"race{(v1, v2, g)} ==> {race(v1, v2, g)}")
