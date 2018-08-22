# https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import *

z = complex(input())
# print(z.conjugate())

x = z.real
y = z.imag
r = abs(complex(x, y))    # modulus of z
phi = phase(complex(x, y))    # argument of z
print(r)
print(phi)
