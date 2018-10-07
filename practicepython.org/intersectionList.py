# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

a = [2, 0, 4, 5, 2, 4, 8, 51, 14, 18, 10, 6, 3]
print(a)

b = random.sample(range(20), 10)
print(b)

c = [x for x in set(a) if x in b]
print(c)
