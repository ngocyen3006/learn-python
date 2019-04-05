# https://leetcode.com/problems/peak-index-in-a-mountain-array/

def peakIndexInMountainArray(A):
    return A.index(max(A))


if __name__ == '__main__':
    print(peakIndexInMountainArray([0, 1, 0]))  # 1
    print(peakIndexInMountainArray([0, 2, 1, 0]))  # 1
