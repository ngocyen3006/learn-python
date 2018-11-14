def ack(m, n):
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


res = ack(3, 4)
print(res)
# res1 = ack(4, 5)
# print(res1)
