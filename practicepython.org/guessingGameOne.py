# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

r = random.randint(1, 9)

n = 0
count = 0

while True:
    n = input("Enter a guess number: ")

    if n.lower() == "exit":
        print("So unfortunately!")
        break

    count = count + 1
    try:
        if int(n) < r:
            print("Too low!")
        elif int(n) > r:
            print("Too high!")
        else:
            print("Exactly right.")
            print("You guess {} times.".format(count))
            break
    except ValueError:
        print("Please input a number!\n")
        continue
