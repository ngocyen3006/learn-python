def drawGameBoard(n):
    i = 0
    while i < n:
        print(" ---" * n)
        print("|   " * n + "|")
        i += 1
    print(" ---" * n)


if __name__ == '__main__':
    size = int(input("What size of game board? "))
    drawGameBoard(size)
