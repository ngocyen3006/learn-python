# https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(J: str, S: str):
    L = " ".join(S).split(" ")
    s = 0
    for c in J:
        s += L.count(c)
    return s

    # Method 2
    # return sum([i in J for i in S])


if __name__ == '__main__':
    j = "aA"
    s = "aAAbbbb"
    print(numJewelsInStones(j, s))
    print("-" * 20)
    j = "z"
    s = "ZZ"
    print(numJewelsInStones(j, s))
    print("-" * 20)
