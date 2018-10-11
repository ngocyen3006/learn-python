import random


def cowBull(number, guess):
    if len(number) > len(guess):
        length = len(guess)
    else:
        length = len(number)
    cow = length
    bull = 0
    for i in range(length):
        if number[i] == guess[i]:
            cow -= 1
            bull += 1
    return (cow, bull)


if __name__ == "__main__":
    # random 4 digit number
    number = str(random.randint(1000, 9999))
    print(number)

    count = 0  # count guess times
    loop = True
    while loop:
        # user guess a number
        print("Give me your guess!")
        guess = input()
        count += 1
        if guess.lower() == "exit":
            loop = False
        elif len(guess) > len(number):
            print("Your guess number is  too large, try again.")
        else:
            result = cowBull(number, guess)
            if result[1] == len(number):
                print("You win the game with {} bulls after {} guess times.".format(result[1], count))
                loop = False
            else:
                print("You have {} cows, and {} bulls.".format(result[0], result[1]))
                print("Your guess isn't quite right, try again.")
