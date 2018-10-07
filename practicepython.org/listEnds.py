# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

import random

a = random.sample(range(20), 7)
# a = []
# a = None
print(a)


def listEnds(a):
    if a == [] or a == None:
        return None

    return [a[0], a[-1]]


print(listEnds(a))
