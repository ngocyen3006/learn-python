# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

def lessThanFive(arr, n):
    listLessThan = []
    for i in arr:
        if i < n:
            listLessThan.append(i)
    return listLessThan


arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = 5
print(lessThanFive(arr, n))
