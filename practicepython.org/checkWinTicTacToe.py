# http://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

def checkWinGame(a):
    # check win is a row
    for j in range(3):
        if a[j][0] == a[j][1] == a[j][2] and a[j][0] != 0:
            return a[j][0]

    # check win is a column
    for i in range(3):
        if a[0][i] == a[1][i] == a[2][i] and a[0][i] != 0:
            return a[0][i]

    # check win is a diagonal
    if (a[0][0] == a[1][1] == a[2][2] or a[2][0] == a[1][1] == a[0][2]) and a[1][1] != 0:
        return a[1][1]
    return 0
