# https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    namelist = s.split(" ")
    name = ""
    for i in namelist:
        name = name + " " + i.capitalize()
    return name.strip()


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
    print(result)
