# Power of 4
import math


def is_power_of_four(number):
    x = 1
    while x < number:
        x = x << 2
    return x == number


if __name__ == '__main__':
    testcase = {1: True,
                4: True,
                16: True,
                8: False,
                64: True,
                24: False,
                5: False,
                256: True,
                1024: True,
                1020: False,
                19: False}
    for k, v in testcase.items():
        print(f"is_power_of_four({k}) = {is_power_of_four(k) == v}")
        print(f"is_power_of_four({k}) = {is_power_of_four(k)}")
        print("-" * 25)
