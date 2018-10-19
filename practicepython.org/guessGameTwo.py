# http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

import random


def guessGame():
    low = 0
    high = 100
    count = 0

    # r = int((low + high) // 2)
    r = random.randint(low, high)
    print(f"I guess the number you think is: {r}")

    print("Is it True, too low, or too high? ")
    result = input()

    while result != "true" and result != "exit":
        while result.lower() == "too low":
            low = r + 1
            # r = int((low + high) // 2)
            r = random.randint(low, high)
            print(f"I guess the number is: {r}")
            result = input()
            count += 1

        while result.lower() == "too high":
            high = r - 1
            # r = int((low + high) // 2)
            r = random.randint(low, high)
            print(f"I guess the number is: {r}")
            result = input()
            count += 1

    if result.lower() == "exit":
        return

    if result.lower() == "true":
        print(f"This number is {r} with {count} guesses.")
        return


if __name__ == '__main__':
    guessGame()
