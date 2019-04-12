# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

def numPairsDivisibleBy60(time):
    res = 0
    n = len(time)
    list_time = {}
    for i in range(n):
        time[i] = 60 - time[i] % 60
        list_time.setdefault(time[i], 0)
        list_time[time[i]] += 1
    for k in list_time.keys():
        if k == 30 or k == 0:
            res += list_time[k] * (list_time[k] - 1) // 2

        elif k > 0 and k < 30:
            if 60 - k in list_time.keys():
                res += list_time[k] * list_time[60 - k]

    return res


def test():
    ip, op = [30, 20, 150, 100, 40], 3
    print(numPairsDivisibleBy60(ip), op)
    print('-' * 10)

    ip, op = [60, 60, 60], 3
    print(numPairsDivisibleBy60(ip), op)


if __name__ == '__main__':
    test()
