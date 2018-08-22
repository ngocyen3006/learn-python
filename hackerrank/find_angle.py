# https://www.hackerrank.com/challenges/find-angle/problem

ab = int(input())
bc = int(input())
from math import *

# Method 1
ac = sqrt(ab ** 2 + bc ** 2)
mc = ac / 2
cosA = ab / ac
bm = sqrt((ab ** 2) + (mc ** 2) - (2 * ab * mc * cosA))
cosMBC = (bm ** 2 + bc ** 2 - mc ** 2) / (2 * bm * bc)
MBC = round(acos(cosMBC) * 180 / pi)
print("%d°" % MBC)

# Method 2
mi = ab / 2     # I is midpoint of BC, MI is midline
bi = bc / 2
tanMBC = mi / bi
degreesMBC = round(atan(tanMBC) * 180 / pi)
print("%d°" % degreesMBC)
