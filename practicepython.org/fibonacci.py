# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fibList(n):
    if n < 0:
        return None
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    a = [1, 1]
    for i in range(2, n):
        a.append((a[i - 1] + a[i - 2]))
    return a


n = 8
print(fibList(n))
